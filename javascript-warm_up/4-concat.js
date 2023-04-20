#!/usr/bin/node

const args = process.argv;
if (args[2] == null) {
  console.log("undefined", end = "");
}else {
  console.log(args[2], end ="");
}
console.log ("is", end = "");
if (args[3] == null) {
  console.log("undefined", end = "");
}else {
  console.log(args[3]);
}
