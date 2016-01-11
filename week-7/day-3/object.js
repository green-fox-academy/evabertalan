'use strict';

var humwee = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 20000
};

function oldride(car, km) {
  car.km += km;
}

oldride(humwee, 200);

console.log(humwee.km);



var humwee2 = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 20000,
  ride: ride
};

function ride(km) {
  this.km += km;
}

humwee2.ride(200);

console.log(humwee2.km);



var humwee3 = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 20000,
  ride: function(km){
    this.km +=km
  }
};

humwee3.ride(200);

console.log(humwee3.km);
