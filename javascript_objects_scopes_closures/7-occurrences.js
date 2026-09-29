#!/usr/bin/node

function nbOccurences (list, searchedElement) {
  return list.filter((item) => item === searchedElement).length;
}

module.exports = { nbOccurences };
