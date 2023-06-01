#!/usr/bin/node
//Star wars

const request = require('request');

function fetch_char(url_char) {
  var option_a = {
	  url: url_char,
	  method: 'GET'
  }
  var n;
  request(option_a, function(err, res, body) {
    let results = JSON.parse(body);
    n = results.name;
  });
  return n;
}
var option_b = {
	url: "https://swapi.dev/api/films/" + process.argv[2],
	method: 'GET'
}
function fetch_film(){
  var name_list = [];
  var d = []
  request(option_b, function(err, res, body) { 
    let data = JSON.parse(body);
    d = data.characters;
  });
  for (let i = 0; i < d.length; i++) {
    name_list.push(fetch_char(d[i]));
  }
  for (let i = 0; i < name_list.length; i++) {
    console.log(name_list[i]);
  }
}
fetch_film();
