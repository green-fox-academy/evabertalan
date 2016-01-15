'use strict';
var express = require('express');
var url = require('url');
var app = express();

app.use(express.static("public"));

// var item =

app.get('/add', function(req, res) {
  var urlParts = url.parse(req.url, true);
  var query = urlParts.query;
  var a = parseInt(query['a']);
  var b = parseInt(query['b']);
  var result = a + 'nem hiszem el';

  console.log(a, b);
  console.log(result);

  res.send(result.toString() + '\n');
});


app.listen(3000);
