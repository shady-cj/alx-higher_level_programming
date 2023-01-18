#!/usr/bin/node
/**
 * a script that prints all characters of a star wars movie
 * Usage: ./100-starwars_characters id
 */

if (process.argv.length < 3) process.exit();
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, res, body) {
  if (error) { console.log(error); } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    for (const characterUrl of characters) {
      request(characterUrl, (error, res, body) => {
        if (error) {
          console.error(error);
        } else {
          const karacter = JSON.parse(body);
          console.log(karacter.name);
        }
      });
    }
  }
});
