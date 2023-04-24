#!/usr/bin/node

const file_name = process.argv[2];
const fs = require('fs');

fs.readFile(file_name, 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
