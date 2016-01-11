'use strict';

var pairs = {
  0 : '',
  1 : 'I',
  2 : 'II',
  3 : 'III',
  4 : 'IV',
  5 : 'V',
  6 : 'VI'
}

function arabic2roman(arabic) {
  return pairs[arabic]
}

module.exports = arabic2roman;
