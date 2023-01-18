#!/usr/bin/node
/**
 * a script that gets the content of a web page
 * and stores it in a file
 * arg1: url to scrape
 * arg2: filepath
 */

if (process.argv.length < 4) process.exit();
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, res, body) {
  if (error) { console.log(error); } else {
    fs.writeFile(process.argv[3], body, { encoding: 'utf8' }, (err) => {
      if (err) { console.error(err); }
    });
  }
});
