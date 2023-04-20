#!/usr/bin/node

const args = process.argv;
if (args[2] == null) {
  console.log("undefined");
}else {
  console.log(args[2]);
}
console.log ("is");
if (args[3] == null) {
  console.log("undefined");
}else {
  console.log(args[3]);
}
