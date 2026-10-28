import io
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from serve import HERE, Handler


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = 4461

    def request(self, method, path, host=None, directory=HERE):
        handler = Handler.__new__(Handler)
        handler.path = path
        handler.command = method
        handler.headers = {"Host": host or "localhost:%d" % self.port}
        handler.server = SimpleNamespace(server_port=self.port)
        handler.directory = str(directory)
        handler.request_version = "HTTP/1.1"
        handler.wfile = io.BytesIO()
        handler.log_request = lambda *args: None
        handler.log_error = lambda *args: None
        if method == "GET":
            handler.do_GET()
        else:
            handler.do_HEAD()
        response = handler.wfile.getvalue().split(b"\r\n\r\n", 1)[0].decode("latin-1")
        lines = response.split("\r\n")
        status = int(lines[0].split()[1])
        headers = dict(line.split(": ", 1) for line in lines[1:] if ": " in line)
        return status, headers

    def test_static_allowlist(self):
        for method in ("GET", "HEAD"):
            for path in ("/", "/index.html", "/questions.json"):
                with self.subTest(method=method, path=path):
                    self.assertEqual(self.request(method, path)[0], 200)
            for path in ("/.git/HEAD", "/.git/config", "/serve.py", "/build.sh",
                         "/tests/test_server.py", "/%2egit/HEAD"):
                with self.subTest(method=method, path=path):
                    self.assertEqual(self.request(method, path)[0], 404)
            self.assertEqual(self.request(method, "/index.html", "evil.example:%d" % self.port)[0], 403)
            self.assertEqual(self.request(method, "/serve.py", "evil.example:%d" % self.port)[0], 403)

    def test_no_directory_listing_or_symlink_target(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "serve.py").write_text("private source")
            self.assertEqual(self.request("GET", "/", directory=directory)[0], 404)
            (Path(directory) / "index.html").symlink_to("serve.py")
            self.assertEqual(self.request("GET", "/", directory=directory)[0], 404)
            self.assertEqual(self.request("HEAD", "/index.html", directory=directory)[0], 404)

    def test_security_headers_on_static_and_api_responses(self):
        for method, path in (("GET", "/index.html"), ("HEAD", "/questions.json"),
                             ("GET", "/api/ask"), ("GET", "/serve.py")):
            with self.subTest(method=method, path=path):
                _, headers = self.request(method, path)
                self.assertEqual(headers.get("X-Content-Type-Options"), "nosniff")
                csp = headers.get("Content-Security-Policy", "")
                self.assertIn("frame-ancestors 'none'", csp)
                self.assertIn("object-src 'none'", csp)
                self.assertIn("script-src 'self' 'sha256-", csp)
                self.assertNotIn("script-src 'self' 'unsafe-inline'", csp)


if __name__ == "__main__":
    unittest.main()
