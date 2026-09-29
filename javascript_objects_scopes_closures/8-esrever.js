#!/usr/bin/node

function esrever (list) {
  const result = [];
  for (let i = list.length - 1; i >= 0; i -= 1) {
    result.push(list[i]);
  }
  return result;
}

module.exports = { esrever };
