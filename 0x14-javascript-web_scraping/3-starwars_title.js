#!/usr/bin/node
/**
 * a script that prints the title of a star wars movie using the
 * star wars api with the request module
 * Usage: ./3-starwars_title.js id
 */

if (process.argv.length < 3) process.exit();
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, res, body) {
  if (error) { console.log(error); } else {
    const parsedBody = JSON.parse(body);
    console.log(parsedBody.title);
  }
});
