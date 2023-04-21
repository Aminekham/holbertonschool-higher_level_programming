#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 && h <= 0) {
      return(undefined, undefined);
    }
    else if (h <= 0) {
        return(undefined, undefined);
    }
    else if (w <= 0) {
        return(undefined, undefined);
    }
    else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;