'use strict';

var fs = require('fs');

function readAlmaTxt(callback) {
  fs.readFile('alma.txt', function(err, content){
    callback(String(content));
  });
}


readAlmaTxt(function(content) {
  console.log(content);
})
