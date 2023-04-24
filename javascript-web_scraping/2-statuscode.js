#!/usr/bin/node
const link = process.argv[2];

async function getting_status(link) {
  const fetch = require('fetch');
  const fetch_url = await fetch(link);
  console.log(fetch_url.status);
}

getting_status(link);
