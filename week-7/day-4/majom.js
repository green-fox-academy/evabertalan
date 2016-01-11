'use strict';
console.log('mukodik');

var cim = document.querySelector('h1');
console.log(cim);

// cim.style.backgroundColor = 'pink';
cim.classList.add('piros');

var majomKep = document.querySelector('img');

majomKep.setAttribute('src', 'https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg')


var bodyvaltozoban = document.querySelector('body');

function kepcsinalo (src) {
  var ujkep = document.createElement('img');

  ujkep.setAttribute('src', src);

  bodyvaltozoban.appendChild(ujkep);
}

// for (var i = 0; i < 10; i++) {
//   kepcsinalo('https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg');
// }


var kepek = ['http://www.the666.com/fotos/numero%201.jpg', 'https://blognumbers.files.wordpress.com/2010/09/2.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Classic_alphabet_numbers_3_at_coloring-pages-for-kids-boys-dotcom.svg/220px-Classic_alphabet_numbers_3_at_coloring-pages-for-kids-boys-dotcom.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/6/6c/Classic_alphabet_numbers_4_at_coloring-pages-for-kids-boys-dotcom.svg', 'http://simplythemag.com/dev/wp-content/uploads/2015/07/5.jpg', 'http://vignette3.wikia.nocookie.net/opartshunter/images/1/18/6.jpg/revision/latest?cb=20130603053127', 'http://www.wpclipart.com/signs_symbol/alphabets_numbers/outlined_numbers/outline/number_7_outline.png', 'http://www.wpclipart.com/signs_symbol/alphabets_numbers/outlined_numbers/pink/number_8_pink.png', 'https://blognumbers.files.wordpress.com/2010/09/9.jpg', 'http://1.bp.blogspot.com/-zAghBRP-Pc8/U_5JiZe9wgI/AAAAAAAACJs/ifpAjZ3tuL8/s1600/600px-MA_Route_10.svg.png']


for (var i = 0; i < kepek.length; i++) {
  kepcsinalo(kepek[i]);
}

var gomb = document.querySelector('.csinal');

gomb.addEventListener('click', function() {
  kepcsinalo('https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg');
  //console.log('kattintottam');
  // alert('kattintottam');
});

window.addEventListener('scroll', function() {
  console.log('scroll', window.scrollY);
});

var cicagomb = document.querySelector('.cica');

var kutyagomb = document.querySelector('.kutya');

var valtoskep = document.querySelector('.cicakutyakep');

kutyagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTcDXhwfulGsULUsyoijHKd99T9Nt2xUlARsYl9f7GGYLycDlOHyQ');
});

cicagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Domestic_cat_cropped.jpg');
});
