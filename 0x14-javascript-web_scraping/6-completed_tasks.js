#!/usr/bin/node
/**
 * a script that computes the number of tasks completed by
 * user id.
 * arg1: url to scrape
 */

if (process.argv.length < 3) process.exit();
const request = require('request');

request(process.argv[2], function (error, res, body) {
  if (error) { console.log(error); } else {
    const todos = JSON.parse(body);
    const userTasks = {};
    for (const todo of todos) {
      if (todo.completed) {
        const tasks = userTasks[todo.userId];
        userTasks[todo.userId] = tasks ? tasks + 1 : 1;
      }
    }
    console.log(userTasks);
  }
});
