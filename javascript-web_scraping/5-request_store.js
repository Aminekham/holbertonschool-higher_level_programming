#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const filename = process.argv[3];
request(link, function(error, body, status){
  fs.writeFile(filename, body, err =>{
    if (err) throw err;
  });
});
