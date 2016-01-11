'use strict';

var kids = [
  {name: 'Tibor', candies: 4},
  {name: 'Szabi', candies: 3},
  {name: 'Laci', candies: 5},
  {name: 'Aurel', candies: 8},
  {name: 'Steve', candies: 12}
];

function getRichestKidsName(kids) {
  var richestKid=kids[0]
  for (var i=1; i < kids.length; i++) {
    if (kids[i].candies > richestKid.candies) {
      richestKid=kids[i];
    }
  }
  return richestKid.name;
}




function getRichestKidsName2(kids) {
  var richestKid = kids[0];
  kids.forEach(function(currentKid) {
    if (currentKid.candies > richestKid.candies)
    richestKid = currentKid;
  })
  return richestKid.name
};


console.log(getRichestKidsName2(kids));
