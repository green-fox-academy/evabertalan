'use strict'

function createRequest(method, url, data, callback) {
  var todoRequest = new XMLHttpRequest();
  todoRequest.open(method, url);
  todoRequest.setRequestHeader('Content-type', 'application/json');
  todoRequest.send(data);
  todoRequest.onreadystatechange = function () {
    console.log('status: ', todoRequest.readyState);
    if (todoRequest.readyState === 4) {
      callback(todoRequest.response);
    }
  };
}
