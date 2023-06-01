#!/usr/bin/node
//fetches Star wars characters of a movie

const request = require('request');

url = "https://swapi.dev/api/films/" + process.argv[2],

request(url, function(err, res, body) {
  if (error == null) {
    let results = JSON.parse(body);
    let names = results.name;
    if (names) {
      fetch_char(names);
    }
  } else {
    console.log(error);
  }
});
function fetch_char(names){
  for(let i = 0; i < names.length; i++) {
    request(names[i], function(err, res, body) { 
      if (error == null) {
        let data = JSON.parse(body);
        console.log(data.name);
      }
      else {
        console.log(error)
      }
    });
  }
}
