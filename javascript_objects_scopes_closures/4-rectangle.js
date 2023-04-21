#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
      if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
        return;
      }
      this.width = w;
      this.height = h;
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
    rotate () {
      this.height = this.height - this.width;
      this.width = this.width + this.height;
      this.height = this.width - this.height;
    }
    double () {
      this.height = this.height * 2;
      this.width = this.width * 2;
    }
  }
module.exports = Rectangle;
  