#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor(size) {
    super(Rectangle.width) = size;
    super(Rectangle.height) = size;
  }
}
module.exports = Square;