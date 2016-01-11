'use strict';

var list = [1,2,3,4,5];
var sum = 0

for (var i = 0; i < list.length; i++){
  sum=sum+list[i];
}

console.log(sum);


function summ(numbers) {
  var output = 0
  for (var j = 0; j < numbers.length; j++) {
    output += numbers[j];
  }
  return output
}

console.log(summ([1,2,3,4,5]));
