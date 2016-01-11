'use strict';

var input = 'kacsa';
var output = '';

for(var i = input.length-1; i >= 0 ; i--) {
  output +=input[i];
}

console.log(output);


//recursive

function reverseRecursive(input, i) {
  if (i < 0) {
    return ''
  } else {
    return input[i] + reverseRecursive(input, i-1)
  }
}

console.log(reverseRecursive('kacsa', 4));


//reverse2
function reverse2(input) {
  return reverseRecursive(input, input.length-1)
}
