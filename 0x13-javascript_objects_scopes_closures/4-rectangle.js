#!/usr/bin/node
// Defines a Rectangle//

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print the Rectangle
  print () {
    let rect = '';
    for (let i = 0; i < this.width; i++) {
      rect += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }

  // Method that exchanges the width and the height of the rectangle
  rotate () {
    const holder = this.height;
    this.height = this.width;
    this.width = holder;
  }

  // Method the width and height of the Rectangle by 2
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
