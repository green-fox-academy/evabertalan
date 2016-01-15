'use strict';

function runIn5seconds(callback) {
  setTimeout(callback, 5000);
}

runIn5seconds(function() {
  console.log('jeee');
});
