'use strict'

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var todoContainer = document.querySelector('.todo-container')
var todoInput = document.querySelector('.todo-input')
var addTodo = document.querySelector('.add-todo')
var removeAllTodo = document.querySelector('.remove-all-todo')


var listCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(todoItem) {
    var newTodoItem = document.createElement('p');
    newTodoItem.setAttribute('id', todoItem.id)
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);

    var newDeleteButton = document.createElement('button')
    newDeleteButton.innerText = 'Remove'
    newDeleteButton.setAttribute('class', 'remove-this' )
    newDeleteButton.setAttribute('id', todoItem.id)
    todoContainer.appendChild(newDeleteButton);

  })
}

var refresh = function() {
  todoContainer.innerHTML = ""
  createRequest('GET', url, {}, listCallback)
}

addTodo.addEventListener('click', function() {
  var newTodo = JSON.stringify({text: todoInput.value});
  var createTodoCallback = function (response) {
    refresh();
  }

  createRequest('POST', url, newTodo, createTodoCallback);
});

removeAllTodo.addEventListener('click', function() {
  todoContainer.innerHTML = ""
});

var removeElement = document.querySelector('.todo-container');

removeElement.addEventListener('click', function(e) {
  var id = e.target.getAttribute("id");
  createRequest('DELETE', url +'/' + id, undefined, refresh)
});

refresh()
