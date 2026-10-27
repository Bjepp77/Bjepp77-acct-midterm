#!/usr/bin/env python3
"""Local server for the prep tool: the static site plus an Ask Claude box.

    python3 serve.py [--port 4183]

Binds to 127.0.0.1 only. POST /api/ask runs `claude -p` (Claude Code's headless mode,
using its existing login) with every tool off, so a question can only produce text.
The study guide and cheat sheet go in as context. GitHub Pages has no /api/ask, so the
box stays hidden there.
"""
import argparse
import json
import subprocess
import tempfile
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_Q = 4000
MAX_TURNS = 3          # earlier question/answer pairs sent with a follow-up
TIMEOUT = 180
LOCK = threading.Lock()  # one claude run at a time
EMPTY = tempfile.mkdtemp(prefix="acct-ask-")  # cwd with no project files or CLAUDE.md

SYSTEM = ("You are a tutor for a first-year MBA managerial accounting course (MBA 502, "
          "Exam 1: cost behaviour, CVP, job and process costing, cost allocation, Blocher "
          "ch. 3, 8, 9). The student is studying, not sitting the exam. Answer in plain "
          "English, short, plain text with no markdown (no asterisks or # headings). For numbers, show the setup and each step. Use the course notes "
          "below when they apply and say so; if they do not cover it, say that and answer "
          "from general accounting.\n\n")


def context():
    parts = []
    for name in ("cheat-sheet.md", "study-guide.md"):
        p = HERE / name
        if p.exists():
            parts.append("=== %s ===\n%s" % (name, p.read_text(encoding="utf-8")))
    return SYSTEM + "\n\n".join(parts)


def ask(question, history):
    turns = "".join("Earlier question: %s\nYour answer: %s\n\n" % (h["q"], h["a"])
                    for h in history[-MAX_TURNS:])
    cmd = ["claude", "-p", "--tools", "", "--strict-mcp-config", "--setting-sources", "",
           "--no-session-persistence", "--model", "sonnet", "--system-prompt", context()]
    r = subprocess.run(cmd, input=turns + question, capture_output=True, text=True,
                       timeout=TIMEOUT, cwd=EMPTY)
    if r.returncode != 0:
        print("claude exited %d: %s" % (r.returncode, (r.stderr or r.stdout).strip()[-300:]), flush=True)
        raise RuntimeError("claude exited %d" % r.returncode)
    return r.stdout.strip()


class Handler(SimpleHTTPRequestHandler):
    def local(self):
        host = self.headers.get("Host", "")
        ok = {"127.0.0.1:%d" % self.server.server_port, "localhost:%d" % self.server.server_port}
        return host in ok

    def reply(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if not self.local():
            return self.reply(403, {})
        if self.path == "/api/ask":
            return self.reply(200, {"ok": True})
        return super().do_GET()

    def do_HEAD(self):
        if not self.local():
            return self.reply(403, {})
        return super().do_HEAD()

    def do_POST(self):
        if self.path != "/api/ask":
            return self.reply(404, {"error": "not found"})
        origin = self.headers.get("Origin", "")
        if not self.local() or origin != "http://" + self.headers.get("Host", ""):
            return self.reply(403, {"error": "local page only"})
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            return self.reply(415, {"error": "send JSON"})
        try:
            n = int(self.headers.get("Content-Length", ""))
            if n < 0:
                raise ValueError("negative Content-Length")
            data = json.loads(self.rfile.read(min(n, 200000)))
            q = str(data.get("q", "")).strip()
            hist = [{"q": str(h["q"])[:MAX_Q], "a": str(h["a"])[:8000]}
                    for h in data.get("history", [])][-MAX_TURNS:]
        except (ValueError, KeyError, TypeError, AttributeError):
            return self.reply(400, {"error": "bad request"})
        if not q or len(q) > MAX_Q:
            return self.reply(400, {"error": "question must be 1 to %d characters" % MAX_Q})
        if not LOCK.acquire(blocking=False):
            return self.reply(429, {"error": "still answering the last question"})
        try:
            return self.reply(200, {"answer": ask(q, hist)})
        except subprocess.TimeoutExpired:
            return self.reply(504, {"error": "Claude took too long; try again"})
        except (OSError, RuntimeError) as e:
            print("ask failed: %s" % e, flush=True)
            return self.reply(502, {"error": "Claude failed; see the server terminal"})
        finally:
            LOCK.release()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=4183)
    port = ap.parse_args().port
    srv = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(HERE)))
    print("http://127.0.0.1:%d/" % port)
    srv.serve_forever()


if __name__ == "__main__":
    main()
