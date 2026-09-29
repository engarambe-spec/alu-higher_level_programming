#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const result = {};

    for (let i = 0; i < todos.length; i += 1) {
      const todo = todos[i];
      if (todo.completed) {
        if (result[todo.userId] === undefined) {
          result[todo.userId] = 0;
        }
        result[todo.userId] += 1;
      }
    }

    console.log(result);
  }
});
