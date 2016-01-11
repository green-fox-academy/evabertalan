'use strict';

function greet(name) {
  console.log('Csaaa ' + name + '!');
}

greet('Olga');


var koszontes = greet;

koszontes('Tihamer');




var print = console.log;

function greeter (name, log) {
  log('Szia ' + name)
}

greeter('Enci', print);



var add = function (a, b) {
  return a + b;
}

console.log(add(1, 2));


greeter('Klara', function(text) {
  console.log(text, 'logged by my function');
})
