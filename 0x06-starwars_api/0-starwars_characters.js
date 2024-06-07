#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */

const request = require('request');
const filmID = Number(process.argv[2]);

if (isNaN(filmID)) throw Error('Argument must be a number');

const URI = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

request.get(URI, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);

    const promises = [];
    for (const character of data.characters) {
      promises.push(await new Promise((resolve, reject) => {
        request.get(character, (error, response, body) => {
          if (error) reject(error);
          if (response.statusCode === 200) {
            const person = JSON.parse(body);
            resolve(person.name);
          }
        });
      }));
    }

    Promise.all(promises)
      .then(allPromises => {
        allPromises.forEach(name => {
          console.log(name);
        });
      })
      .catch((err) => {
        console.error(err);
      });
  }
});
