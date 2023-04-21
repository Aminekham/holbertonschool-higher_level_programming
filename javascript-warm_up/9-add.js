#!/usr/bin/node

args = proecess.argv;
function add(a, b){
  console.log(parseInt(a) + parseInt(b));
}

add(args[2], args[3])