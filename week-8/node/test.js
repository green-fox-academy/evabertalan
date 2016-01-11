'use strict';

var tape = require('tape');

var arabic2roman = require('./kata');

tape('roman converter', function(t) {
  t.equal(arabic2roman(0), '');
  t.equal(arabic2roman(1), 'I')
  t.equal(arabic2roman(2), 'II')
  t.equal(arabic2roman(4), 'IV')
  t.equal(arabic2roman(5), 'V')
  t.equal(arabic2roman(6), 'VI')
  t.end();
});
