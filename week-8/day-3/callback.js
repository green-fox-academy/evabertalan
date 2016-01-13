'use strict'

function createRequest(method, url, data, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open(method, url);
  probaRequest.setRequestHeader('Content-type', 'application/json');
  probaRequest.send(data);
  probaRequest.onreadystatechange = function () {
    console.log('allapot: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}
