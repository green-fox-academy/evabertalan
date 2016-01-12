'use strict';

var fs = require('fs');

var content = fs.readFileSync('alma.txt');
//ha readFileSync addig all amig vegig nem hajtotta, ezert ezt nem haszna;juk, hanme read file, mert az alatt tud futni a program

console.log(content.toString());
//console.log(String(content));
