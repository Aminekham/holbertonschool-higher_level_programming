#!/usr/bin/node

const fs = require('fs');
const name = process.argv[2];
const text = process.argv[3];

fs.writeFile(name, text, err => {
  if (err) throw err;
});
