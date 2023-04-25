#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const filename = process.argv[3];
request(link, function(error, body, status){
  text = JSON.parse(body)
  fs.writeFile(filename, text.body, 'utf-8', err =>{
    if (err) throw err;
  });
});
