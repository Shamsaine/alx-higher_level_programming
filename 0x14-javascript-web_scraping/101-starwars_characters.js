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
    const characterNames = [];

    characters.forEach((characterUrl, index) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.log(charError);
        } else if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          characterNames[index] = character.name;

          if (characterNames.length === characters.length && !characterNames.includes(undefined)) {
            characterNames.forEach(name => console.log(name));
          }
        } else {
          console.log(`Error: ${charResponse.statusCode}`);
        }
      });
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
