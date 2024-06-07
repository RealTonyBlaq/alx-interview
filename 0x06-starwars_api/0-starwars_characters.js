#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */

const request = require('request');
const filmID = process.argv[2];

try {
    const id = Number(filmID);
} catch (err) {
    console.error(`${}')
}
const URI = `https://swapi-api.alx-tools.com/films/${}`
