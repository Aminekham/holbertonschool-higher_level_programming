#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
request(link, function (error, body, status) {
  parsed_json = JSON.parse(body);
  list = parsed_json.results;
  chars = list[0].characters;
  let count = 0;
  for (let i; i < chars.length; i++) {
    if (chars[i] == "https://swapi-api.hbtn.io/api/people/18/"){
      count = count + 1;
    }
  }
  console.log(count);
});
