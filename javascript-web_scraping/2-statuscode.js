#!/usr/bin/node
const link = process.argv[2];

fetch(link).then(Response => {
  console.log(Response.status);
});
