#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
request(link, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (body.trim().length === 0) {
    console.error('Empty response received');
    return;
  }
  const parsed_json = JSON.parse(body);
  const list = parsed_json.results;
  for(let j = 0; j < list.length; j++){
    const chars = list[j].characters;
    let count = 0;
    for (let i=0; i < chars.length; i++) {
      if (chars[i] == "https://swapi-api.hbtn.io/api/people/18/"){
        count = count + 1;
      }
    }
  }
  console.log(count);
});
