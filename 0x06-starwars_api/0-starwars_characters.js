#!/usr/bin/node
//fetches Star wars characters of a movie

const request = require('request');

var option_a = {
  url: "https://swapi.dev/api/films/" + process.argv[2],
  method: 'GET'
}
request(option_a, function(err, res, body) {
  let results = JSON.parse(body);
  let nm = results.name;
  if (nm) {
    fetch_char(0, nm, nm.length);
  }
});
function fetch_char(index, ch, len){
  for(let i = 0; i < len; i++) {
    request(ch[index], function(err, res, body) { 
      let data = JSON.parse(body);
      console.log(data.name);
    });
  }
}
