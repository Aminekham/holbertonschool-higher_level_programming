#!/usr/bin/node
const link = process.argv[2];
const request = require('request');
request(link, function print_status(response){
  console.log(response.statusCode);
});