'use strict';

var fs = require('fs');

try {
  var content = sf.readFileSync('korte.txt')
} catch (e) {
  content = 'para volt'
}

console.log(String(content));
