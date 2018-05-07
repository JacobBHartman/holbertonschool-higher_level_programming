#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let rowOutput = '';
      for (let j = 0; j < this.width; j++) {
        rowOutput += 'X';
      }
      console.log(rowOutput);
    }
  }
}
module.exports = Rectangle;