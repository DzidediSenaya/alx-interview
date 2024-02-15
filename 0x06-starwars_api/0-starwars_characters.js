#!/usr/bin/node

const request = require('request');

const requestCharacters = (characterUrls, index) => {
  if (index === characterUrls.length) return;
  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    requestCharacters(characterUrls, index + 1);
  });
};

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const chars = JSON.parse(body).characters;
  requestCharacters(chars, 0);
});
