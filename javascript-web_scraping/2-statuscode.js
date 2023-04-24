#!/usr/bin/node
const link = process.argv[2];
const request = require('request');
request(link, function print_status(error, response, body){
  if (error) {
    console.error(error);
  }
  console.log('code:',response.statusCode);
});