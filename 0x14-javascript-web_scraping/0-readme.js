#!/usr/bin/node
const fs = require('fs');
const url = './' + process.argv[2]

fs.readFile(url, 'utf8', function(err, data) {
  if (err) throw err;
  console.log(data);
});
