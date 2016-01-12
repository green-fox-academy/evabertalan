"use strict";


var count= 0;

var interval = setInterval (function () {
  count ++
  console.log('je-je-je', count);
}, 500);

setTimeout(function() {
  console.log('Booom');
  clearInterval(interval);
}, 5000);


setTimeout(function() {
  for(var i = 0; i < 1234567118; i++) {
// ha ey itt van lefoglalja annira, hogz elcsusyik a szamlalo es a boom mar a 7dik masodpercel kiirodik
  }
}, 2000)
