#!/usr/bin/node

function converter (base) {
  return (number) => number.toString(base);
}

module.exports = { converter };
