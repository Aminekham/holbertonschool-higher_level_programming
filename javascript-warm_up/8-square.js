#!/usr/bin/node 

const args = process.argv;
if (args[2] == null || Number.isInteger(args[2]) == false) {
  console.log("Missing size");
}else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    for(let i = 0; i < parseInt(args[2]); i++) {
      console.log('%s', 'X');
    }
    console.log('');
  }
}