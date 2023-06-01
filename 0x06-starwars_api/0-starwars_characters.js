#!/usr/bin/node
//fetches Star wars characters of a movie

const request = require('request');

url = "https://swapi.dev/api/films/" + process.argv[2];

request(url, function(error, response, body) {
  if (error == null) {
    let results = JSON.parse(body);
    let names = results.characters;
    if (names) {
      fetch_char(0, names);
    }
  } else {
    console.log(error);
  }
});
function fetch_char(j, names){
  if (j < names.length) {
    request(names[j], function(err, res, body) { 
      if (err == null) {
        const data = JSON.parse(body);
        console.log(data.name);
      }
      else {
        console.log(error);
      }
      j++;
      fetch_char(j, names);
    });
  }
}
