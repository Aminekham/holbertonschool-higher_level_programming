#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
request(link, function(error, body, status) {
  const parsed = JSON.parse(body);
  let dict = {};
  for(let j = 0; j < parsed.length; j++) {
    x = parsed[j].userId;
    if (dict[x] != 0 || !dict[x]){
      dict[x] = 0;
    }
  }
  console.log(dict);
})