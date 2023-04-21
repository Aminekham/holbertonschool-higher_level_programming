#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      this.width = NaN;
      this.height = NaN;
    }
  }
}

module.exports = Rectangle;