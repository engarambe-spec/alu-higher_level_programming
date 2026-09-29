#!/usr/bin/node

const args = process.argv.slice(2).map((a) => parseInt(a, 10));

if (args.length < 2) {
  console.log(0);
} else {
  const sorted = args.slice().sort((a, b) => b - a);
  console.log(sorted[1]);
}
