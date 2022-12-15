#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((entry, index) => entry * index);

console.log(list);
console.log(newList);
