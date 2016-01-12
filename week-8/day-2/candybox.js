'use strict';

var numberOfCandies = 0;

document.querySelector('.create_candies').addEventListener('click', function() {
  numberOfCandies +=1 ;
  document.querySelector('.number_of_candies').innerHTML = numberOfCandies;
});

var numberOfLollipops = 0;

document.querySelector('.buy_lollipop').addEventListener('click', function() {
  if(numberOfCandies >= 10) {
    numberOfLollipops += 1 ;
    document.querySelector('.number_of_lollipops').innerHTML = numberOfLollipops;
    numberOfCandies -= 10;
    document.querySelector('.number_of_candies').innerHTML = numberOfCandies;
  } else {
    console.log('kaka');
  }
});

setInterval (function () {
  var candiesPerSec = Math.floor(numberOfLollipops/10);
  if (numberOfLollipops >= 10) {
    numberOfCandies +=1 * candiesPerSec;
    document.querySelector('.number_of_candies').innerHTML = numberOfCandies;
    candyVelocity()
  }
},1000)


function candyVelocity() {
  var candiesPerSec = Math.floor(numberOfLollipops/10);
  document.querySelector('.cendies_per_sec').innerHTML = candiesPerSec;
}
