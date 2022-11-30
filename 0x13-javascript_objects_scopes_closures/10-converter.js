#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    let conversion = '';
    let quotient = number;
    const hexes = {
      10: 'A',
      11: 'B',
      12: 'C',
      13: 'D',
      14: 'E',
      15: 'F'
    };
    while (quotient > 0) {
      let rem = quotient % base;
      if (rem > 9) {
        rem = hexes[rem];
      }
      conversion = rem.toString() + conversion;
      quotient = Math.floor(quotient / base);
    }
    return conversion;
  };
};
