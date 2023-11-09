#!/usr/bin/node

const axios = require('axios');

// Get Movie ID from Command Line
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script.js <Movie_ID>');
  process.exit(1);
}

// Make API Request
const url = `https://swapi.dev/api/films/${movieId}/`;

axios.get(url)
  .then(response => {
    if (response.status !== 200) {
      console.error(`Error: Unable to fetch data. Status Code: ${response.status}`);
      process.exit(1);
    }

    // Extract Characters
    const characters = response.data.characters;

    // Display Characters Sequentially
    displayCharactersSequentially(characters);
  })
  .catch(error => {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  });

// Display Characters Sequentially
async function displayCharactersSequentially (characters) {
  for (const characterUrl of characters) {
    try {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    } catch (error) {
      console.error(`Error fetching character: ${error.message}`);
    }
  }
}
