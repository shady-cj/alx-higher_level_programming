#!/usr/bin/node
/**
 * a script that prints the number of movies
 * where the character "Wedge Antilles" is present
 * he has the id of 18
 */

if (process.argv.length < 3) process.exit();
const request = require('request');

request(process.argv[2], function (error, res, body) {
  if (error) { console.log(error); } else {
    let count = 0;
    const parsedBody = JSON.parse(body);
    for (const data of parsedBody.results) {
      data.characters.forEach(character => {
        if (Number(character.split('/')[5]) === 18) {
          count++;
        }
      }
      );
    }
    console.log(count);
  }
});
