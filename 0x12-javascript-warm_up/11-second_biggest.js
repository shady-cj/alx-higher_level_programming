#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const slicedList = args.slice(2);
  let largest = null;
  let secondLargest = null;
  for (const el of slicedList) {
    if (largest === null || parseInt(el) > largest) {
      secondLargest = parseInt(largest);
      largest = parseInt(el);
    }
  }
  console.log(secondLargest);
}
