#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};
for (const userId in dict) {
  if (dict[userId] in sortedDict) {
    sortedDict[dict[userId]].push(userId);
  } else {
    sortedDict[dict[userId]] = [userId];
  }
}
console.log(sortedDict);
