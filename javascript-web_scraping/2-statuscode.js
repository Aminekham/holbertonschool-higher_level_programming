#!/usr/bin/node
const link = process.argv[2];
const url_response = fetch(link);

console.log(url_response.status);
