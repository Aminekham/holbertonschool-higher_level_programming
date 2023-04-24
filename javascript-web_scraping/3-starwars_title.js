#!/usr/bin/node

const request = require('request');
id = process.agrv[2];
request('https://swapi-api.hbtn.io/api/films/'+id+'id', function title(error, response, body) {
  console.log(body);
})
