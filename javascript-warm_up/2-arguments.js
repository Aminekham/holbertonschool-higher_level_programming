#!/usr/bin/node

const args = process.argv;
if (args[2] == null) {
  console.log("No argument");
}
else if (args[3] == null) {
  console.log("Argument found");
}
else {
  console.log("Arguments found");
}
