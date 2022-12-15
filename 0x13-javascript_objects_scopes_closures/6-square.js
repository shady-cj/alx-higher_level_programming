#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined || c === null) c = 'X';
    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
