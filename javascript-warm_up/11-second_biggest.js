#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] == null) {
  console.log(0);
}
j = parseInt(args[0])
for (let i = 1; i < length(args); i++) {
  if (j < parseInt(args[i])) {
    f = j;
    j  = parseInt(args[i]);
  }
}
console.log(f);