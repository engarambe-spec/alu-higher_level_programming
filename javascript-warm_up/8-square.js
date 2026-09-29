#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i += 1) {
    let line = '';
    for (let j = 0; j < size; j += 1) {
      line += 'X';
    }
    console.log(line);
  }
}
