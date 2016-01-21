'use strict';

function createCounter() {
  var count = 0;
  return function() {
    count++;
    return count;
  }
}

//var valami = createCounter();
//console.log(valami); ---> [Function]

var counter = createCounter();
console.log(counter()); //---> 1
console.log(counter());
