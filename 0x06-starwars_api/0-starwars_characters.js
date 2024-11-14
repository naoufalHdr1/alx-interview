#!/usr/bin/node

/**
 * Star Wars Characters Module
 *
 * This module retrieves and displays the names of all characters in a specified
 * Star Wars movie, using the Star Wars API.
 */

const request = require('request');

/**
 * Fetches and displays character names from the Star Wars API based on a given movie ID.
 * 
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function fetchAndDisplayCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      displayCharactersInOrder(characterUrls);
    } else {
      console.error(`Error: Received status code ${response.statusCode}`);
    }
  });
}

/**
 * Fetches and displays each character's name in order as listed in the character URLs.
 * 
 * @param {Array<string>} characterUrls - Array of URLs for each character.
 */
function displayCharactersInOrder(characterUrls) {
  const characterPromises = characterUrls.map((url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        } else {
          reject(`Error: Received status code ${response.statusCode} for ${url}`);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => console.log(name));
    })
    .catch((error) => console.error('Error:', error));
}

// Parse command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
} else {
  fetchAndDisplayCharacters(movieId);
}
