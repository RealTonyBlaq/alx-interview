#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */

const request = require('request');
const { json } = require('stream/consumers');
const filmID = process.argv[2];

try {
    const id = Number(filmID);
} catch (err) {
    console.error(`${filmID} must be a number`);
    return;
}

const URI = `https://swapi-api.alx-tools.com/films/${id}`;

request.get(URI, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);

    for (const character of data.characters) {
      const myPromise = new Promise((resolve, reject) => {
        request.get(character, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }
          if (response.statusCode === 200) {
            const person = JSON.parse(body);
            resolve()
          }
        });
      })
    }
  }
});
