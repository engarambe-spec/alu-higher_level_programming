#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const wedgeUrlEnd = '/people/18/';
    let count = 0;

    for (let i = 0; i < data.results.length; i += 1) {
      const film = data.results[i];
      for (let j = 0; j < film.characters.length; j += 1) {
        if (film.characters[j].endsWith(wedgeUrlEnd)) {
          count += 1;
          break;
        }
      }
    }

    console.log(count);
  }
});
