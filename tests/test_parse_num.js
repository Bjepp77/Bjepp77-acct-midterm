const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const html = fs.readFileSync('index.html', 'utf8');
const source = html.match(/function parseNum\(s\)\{[\s\S]*?\n\}/);
assert.ok(source, 'parseNum exists');
const parseNum = vm.runInNewContext(`(${source[0]})`);

for (const value of ['106400xyz', '12.3.4', '1e999', 'Infinity', '', 'abc']) {
  assert.ok(Number.isNaN(parseNum(value)), `${value} should be rejected`);
}
assert.equal(parseNum('$106,400'), 106400);
assert.equal(parseNum(' -2.5e2% '), -250);
console.log('parseNum accepts valid numbers and rejects trailing junk and non-finite values');
