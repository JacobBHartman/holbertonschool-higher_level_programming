#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];

fs.readFile(url, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
