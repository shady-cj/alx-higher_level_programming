#!/usr/bin/node
/*
 * A script that takes a string and writes
 * into a file
 */

const fs = require('fs');

if (process.argv.length < 4) { process.exit(); }
fs.writeFile(process.argv[2], process.argv[3], { encoding: 'utf8' }, (err) => {
  if (err) { console.log(err); }
}
);
