#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.reduce((acc, film) => {
    return acc + film.characters.filter(character => character.includes('/18/')).length;
  }, 0);
  console.log(count);
});
