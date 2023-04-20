#!/usr/bin/node 

const args = process.argv;
if (isNaN(args[2])) {
  console.log("Missing size");
}else if (Number.isInteger(args[2]) == false) {
  console.log("Missing size");
}else {
  for (let i = 0; i < parseInt(args[2]); i++) {
  console.log("X".repeat(parseInt(args[2])));
  }
}