'use strict';

function multiply(a, b){
  return a*b;
}

for (var i = 1; i <= 10; i++) {
  for (var j = 1; j <= 10; j++){
    console.log( j + " * " + i +" = "+multiply(i, j));
  }
  console.log(" ");
}
