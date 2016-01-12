'use strict';

function Game() {
  var _this = this;
  this.numberOfCandies = 0;
  this.numberOfLollipops = 0;

  this.candyCounter = function(a) {
      this.numberOfCandies +=a ;
      document.querySelector('.number_of_candies').innerHTML = this.numberOfCandies;
  }

  this.lollipopCounter = function() {
    this.numberOfLollipops += 1;
    document.querySelector('.number_of_lollipops').innerHTML = this.numberOfLollipops;
  }

  this.checkButtonDisability = function() {
    if (this.numberOfCandies >= 10) {
      document.querySelector('.buy_lollipop').removeAttribute('disabled')
    } else {
      document.querySelector('.buy_lollipop').setAttribute('disabled', 'disabled')
    }
  }

  document.querySelector('.create_candies').addEventListener('click', function() {
    _this.candyCounter(1);
    _this.checkButtonDisability()
  });

  document.querySelector('.buy_lollipop').addEventListener('click', function() {
    if(_this.numberOfCandies >= 10) {
      _this.lollipopCounter()
      _this.candyCounter(-10)
      _this.checkButtonDisability()
    }
  });

  setInterval (function () {
    if (_this.numberOfLollipops >= 10) {
      _this.checkButtonDisability()
      _this.numberOfCandies +=1 * Math.floor(_this.numberOfLollipops/10);
      document.querySelector('.number_of_candies').innerHTML = _this.numberOfCandies;
      _this.candiesPerSec();
    }
  },1000)

  this.candiesPerSec = function() {
    document.querySelector('.cendies_per_sec').innerHTML = Math.floor(_this.numberOfLollipops/10);
  }
}

var game = new Game();
