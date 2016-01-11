'use stict';

function greet (name) {
  console.log('Hi ' + name + '!');
}

greet('Ubul');

greet('Robi', 4, [], {kacsa: 'pulcsiban'});

greet();



function printArgs (a, b, c, d, e) {
  console.log(a, b, c, d, e);
}

printArgs(1, 2, 3)



function double(num) {
  return 2 * num;
}

console.log(double(4));
