#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor(size) {
    super(Rectangle.w) = size;
    super(Rectangle.h) = size;
  }
}
module.exports = Square;