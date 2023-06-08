#!/usr/bin/node
// fetches Star wars characters of a movie

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error == null) {
    const results = JSON.parse(body);
    const names = results.characters;
    if (names) {
      FetchChar(0, names);
    }
  } else {
    console.log(error);
  }
});
function FetchChar (j, names) {
  if (j < names.length) {
    request(names[j], function (error, response, body) {
      if (error === null) {
        const data = JSON.parse(body);
        console.log(data.name);
      } else {
        console.log(error);
      }
      j++;
      FetchChar(j, names);
    });
  }
}
