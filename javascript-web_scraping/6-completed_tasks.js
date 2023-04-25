#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {

    const tasks = JSON.parse(body);
    const completedTasks = {};
    for (let i = 0; i < tasks.length; i++) {
      const task = tasks[i];
      if (task.completed) {
        if (task.userId in completedTasks) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  });
