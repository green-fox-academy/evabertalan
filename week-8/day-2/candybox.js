'use strict';

var numberOfCandies = 0;
var numberOfLollipops = 0;

function candyCounter(a) {
    numberOfCandies +=a ;
    document.querySelector('.number_of_candies').innerHTML = numberOfCandies;
}

function lollipopCounter() {
  numberOfLollipops += 1;
  document.querySelector('.number_of_lollipops').innerHTML = numberOfLollipops;
}

document.querySelector('.create_candies').addEventListener('click', function() {
  candyCounter(1);
});

document.querySelector('.buy_lollipop').addEventListener('click', function() {
  if(numberOfCandies >= 10) {
    lollipopCounter()
    candyCounter(-10)
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
