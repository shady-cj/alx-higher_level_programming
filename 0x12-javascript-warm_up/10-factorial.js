#!/usr/bin/node

const args = process.argv;
if (isNaN(args[2])) {
  console.log(factorial(0));
} else {
  console.log(factorial(parseInt(args[2])));
}

function factorial (x) {
  if (x === 0) return 1;
  else return x * factorial(x - 1);
}
