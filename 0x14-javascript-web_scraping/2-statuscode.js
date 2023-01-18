#!/usr/bin/node
/**
 * getting the status code of an endpoint using the
 * request module
 */

if (process.argv.length < 3) process.exit();
const request = require('request');

request(process.argv[2], function (error, res, body) {
  if (error) { console.log(error); } else { console.log('code:', res.statusCode); }
});
