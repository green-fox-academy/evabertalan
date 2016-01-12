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

function checkButtonDisability() {
  if (numberOfCandies >= 10) {
    document.querySelector('.buy_lollipop').removeAttribute('disabled')
  } else {
    document.querySelector('.buy_lollipop').setAttribute('disabled', 'disabled')
  }
}

document.querySelector('.create_candies').addEventListener('click', function() {
  candyCounter(1);
  checkButtonDisability()
});

document.querySelector('.buy_lollipop').addEventListener('click', function() {
  if(numberOfCandies >= 10) {
    lollipopCounter()
    candyCounter(-10)
    checkButtonDisability()
  }
});

setInterval (function () {
  if (numberOfLollipops >= 10) {
    numberOfCandies +=1 * Math.floor(numberOfLollipops/10);
    document.querySelector('.number_of_candies').innerHTML = numberOfCandies;
    candiesPerSec()
  }
},1000)

function candiesPerSec() {
  document.querySelector('.cendies_per_sec').innerHTML = Math.floor(numberOfLollipops/10);
}
