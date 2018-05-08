#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let tasksCmplt = {};
    let data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i]['completed'] === true) {
        if (tasksCmplt[data[i]['userId']]) {
          tasksCmplt[data[i]['userId']] += 1;
        } else {
          tasksCmplt[data[i]['userId']] = 1;
        }
      }
    }
    console.log(tasksCmplt);
  }
});
