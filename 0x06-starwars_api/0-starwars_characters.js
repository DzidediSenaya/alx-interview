#!/usr/bin/node

const request = require('request');

// Define a recursive function to make requests for each character URL
const requestCharacters = (characterUrls, index) => {
  // Base case: if index exceeds the length of characterUrls, stop recursion
  if (index === characterUrls.length) return;

  // Make a request for the character URL at the current index
  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      
      // Make a recursive call to requestCharacters with the next index
      requestCharacters(characterUrls, index + 1);
    }
  });
};

// Make a request to fetch movie data
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    
    // Start the recursive function with index 0
    requestCharacters(characterUrls, 0);
  }
});
