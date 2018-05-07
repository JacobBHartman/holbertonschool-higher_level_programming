#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X'
    }
    for (let i = 0; i < this.height; i++) {
      let rowOutput = '';
      for (let j = 0; j < this.width; j++) {
        rowOutput += c;
      }
      console.log(rowOutput);
    }
  }
}
module.exports = Square;
