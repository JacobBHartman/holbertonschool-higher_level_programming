#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const apiUrl = process.argv[2];
const file = process.argv[3];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, function (error2) {
      if (error2) {
        console.log(error2);
      }
    });
  }
});
