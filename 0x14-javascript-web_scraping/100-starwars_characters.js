#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.log(charError);
        } else if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.log(`Error: ${charResponse.statusCode}`);
        }
      });
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
