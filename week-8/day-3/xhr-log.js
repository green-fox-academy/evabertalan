'use strict';

var probaRequest = new XMLHttpRequest();
console.log(probaRequest);

var url = 'http://www.greenfoxacademy.com/';
probaRequest.open('GET', url);
//get tipusu lekerest kuls ay oldalra, olyan mintha a bongesyo cimsoraba lenne irva
//post modositas vagy adatkuldes a szerver fele
probaRequest.send();
