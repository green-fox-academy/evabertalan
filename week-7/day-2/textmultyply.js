'use strict'

function textMultyply(szo, szam) {
  var output = ''
  for (var i = 0; i  < szam; i++) {
    output+=szo;
  }
  return output
}


function textMultyply2(szo, szam) {
  return szam > 0 ? szo + textMultyply(szo, szam =1) : '';
}


console.log(textMultyply2('alma', 3));
console.log(textMultyply('alma', 3));
