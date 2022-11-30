#!/usr/bin/node

const fs = require('fs');

const args = process.argv;
if (args.length < 5) {
  console.log('error');
  process.exit();
}

let firstIndex = 2;

const fileA = args[firstIndex++];
const fileB = args[firstIndex++];
const fileC = args[firstIndex];
fs.readFile(fileA, (err, data) => {
  if (err) throw err;
  fs.appendFile(fileC, data.toString(), err => {
    if (err) throw err;
  });
  fs.readFile(fileB, (err, data) => {
    if (err) throw err;
    fs.appendFile(fileC, data.toString(), err => {
      if (err) throw err;
    });
  });
});
