#!/usr/bin/node
//Star wars

/*
async function getter(url) {
  //console.log(url)
  const results = await fetch(url);
  const data = await results.json();
  let n = data.name;
  //console.log(n)
  return n;
}*/
const request = require('request')
var option_a = {
	url: "https://swapi.dev/api/films/" + process.argv[2],
	method: 'GET'
}
request(option_b, function(err, res, body) { 
  let name_list = [];
  let data = JSON.parse(body);
  let d = data.characters;
  console.log(d)
  /*
  for (let i = 0; i < d.length; i++) {
    name_list.push(await getter(d[i]));
  }
  for (let i = 0; i < name_list.length; i++) {
    console.log(name_list[i]);
  }*/
});
fetchPlanets();
