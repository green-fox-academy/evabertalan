'use strict';

function PowerRanger(color) {
  this.color = color;
}

//VERSION 1
// var proto = {isPowerfull: true};
// //objektum leoroklese
// PowerRanger.prototype = proto;

//VERSION 2
function Fighter() {
  this.isPowerfull = true;
}
PowerRanger.prototype = new Fighter;
//END

var yellowRanger = new PowerRanger('yellow');

console.log(yellowRanger.color);
console.log(yellowRanger.isPowerfull);
