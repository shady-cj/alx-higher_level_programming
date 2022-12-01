#!/usr/bin/node

const callMeMoby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
exports.callMeMoby = callMeMoby;
