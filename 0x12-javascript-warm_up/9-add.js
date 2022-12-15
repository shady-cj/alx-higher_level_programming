#!/usr/bin/node
const args = process.argv;

if (isNaN(args[2]) || isNaN(args[3])) {
  console.log('NaN');
} else {
  console.log(add(Number(args[2]), Number(args[3])));
}

function add (a, b) {
  return a + b;
}
