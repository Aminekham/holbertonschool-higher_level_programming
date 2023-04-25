#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
request(link, function(error, body, status) {
  const parsed = JSON.parse(body);
  const dict = {};
  for(let j = 0; j < parsed.length; j++) {
    const id = parsed[j].userId;
    if (dict[id] === undefined) {
      dict[x] = 0;
    }
  }
  console.log(dict);
})