#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2])
if (Number.isInteger(x)) {
    console.log("My number:", x);
}else {
    console.log("Not a number")
}