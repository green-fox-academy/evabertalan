'use strict';

var i = 0;
for ( ; i < 5; ) {
  console.log(i);
  i++;
}


for (var j = 0; j < 6; j++) {
  console.log(j);
}


for (var k = 1; k < 11; k+=2) {
  console.log(k);
}


var dogs = ['Virsli', 'Morzsi', 'Tappancs'];
for (var l = 0; l < dogs.length; l++) {
  console.log(dogs[l]);
}


var student = {
  kor: 6,
  nec: 'timi',
  labmeret: '43'
};

for (var key in student) {
  console.log(key);
  console.log(student[key]);
}
