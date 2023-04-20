#!/usr/bin/node

const args = process.args;
if (args[2] == null) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < parseInt(args[2]); i++) {
  console.log('C is fun');
}
