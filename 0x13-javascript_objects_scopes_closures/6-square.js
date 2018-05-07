#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let rowOutput = '';
        for (let j = 0; j < this.width; j++) {
          rowOutput += c;
        }
        console.log(rowOutput);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
