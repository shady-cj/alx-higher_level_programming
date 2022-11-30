#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let l = list.length - 1; l >= 0; l--) {
    newList.push(list[l]);
  }
  return newList;
};
