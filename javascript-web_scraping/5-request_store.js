#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const filename = process.argv[3];
request(link, function(error, response, body){
  if (error) throw error;
  fs.writeFile (filename, body, 'utf-8', err => {
    if (err) throw err;
  });
});
