#!/usr/bin/node
//Star wars
import fetch from "node-fetch";

async function getter(url) {
  //console.log(url)
  const results = await fetch(url);
  const data = await results.json();
  let n = data.name;
  //console.log(n)
  return n;
}
async function fetchPlanets() { 
  const n = process.argv[2];
  let name_list = [];
  const results = await fetch("https://swapi.dev/api/films/" + n);
  const data = await results.json();
  let d = await data.characters;
  for (let i = 0; i < d.length; i++) {
    name_list.push(await getter(d[i]));
  }
  for (let i = 0; i < name_list.length; i++) {
    console.log(name_list[i]);
  }
} 
fetchPlanets();
