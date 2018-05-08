#!/usr/bin/node
const fs = require('fs');
const url = './' + process.argv[2];
const string = process.argv[3];

fs.writeFile(url, string, function (error) {
  if (error) {
    console.log(error);
  }
});
