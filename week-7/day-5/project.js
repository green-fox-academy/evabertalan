'use strict';

var kep = document.querySelector('img');
var kepek = ['img/1.png',
              'img/2.png', 
              'img/3.png',
               'img/9.png',
              'img/11.png',
              'img/19.png',
              'img/22.png',
              'img/27.png'];
var i = 0;

function kepcsinalo () {
  kep.setAttribute('src', kepek[i]);
}

var visszagomb = document.querySelector('.vissza');
var eloregomb = document.querySelector('.elore');

eloregomb.addEventListener('click', function() {
  if (i===kepek.length-1) {
    i=-1
  };
  i+=1
  kepcsinalo()
});

visszagomb.addEventListener('click', function() {
  if (i===0) {
    i=kepek.length
  };
  i-=1
  kepcsinalo()
});

var thumb = document.querySelector('.thumbnails');

function thumbnailsCreater (src) {
  var ujkep = document.createElement('img');
  ujkep.setAttribute('src', src);
  thumb.appendChild(ujkep);
  ujkep.setAttribute('class', 'kep'+j);
}

for (var j=1; j < kepek.length; j++) {
  thumbnailsCreater(kepek[j]);
}

thumb.addEventListener('click', function(e) {
  kep.setAttribute('src', e.target.src);
  deactivator()
  e.target.classList.add('active');
});

function deactivator() {
  var actives = document.querySelectorAll('.active');
  for (var k=0; k < actives.length; k++) {
    actives[k].classList.remove('active');
  };
}
