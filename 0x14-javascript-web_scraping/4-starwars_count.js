#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let appearances = 0;
    let movieCount = JSON.parse(body).count;
    let desired = 'https://swapi.co/api/people/' + characterId + '/';
    for (let i = 0; i < movieCount; i++) {
      if (JSON.parse(body).results[i].characters.includes(desired)) {
        appearances += 1;
      }
    }
    console.log(appearances);
  }
});
