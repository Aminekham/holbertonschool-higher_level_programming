#!/usr/bin/node

const name = process.argv[2];
const fs = require('fs');

fs.readFile(name, 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
