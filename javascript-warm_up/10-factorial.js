#!/usr/bin/node

args = process.argv;
function fact (a) {
  if (a == 1) {
    return(1);
  }
  return(a * fact(a - 1));
}
console.log(fact(args[2]));
