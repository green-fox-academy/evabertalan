'use strict';

var url = 'http://localhost:3000/todos';
var todoContainer = document.querySelector('.todo-container')
var todoInput = document.querySelector('.todo-input')
var addTodo = document.querySelector('.add-todo')
var removeAllTodo = document.querySelector('.remove-all-todo')
var completedContainer = document.querySelector('.completed-container');


var listCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(todoItem) {
    var newTodoItem = document.createElement('p');
    newTodoItem.setAttribute('id', todoItem.todo_id)
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);

    var newDeleteButton = document.createElement('button')
    newDeleteButton.innerText = 'Remove'
    newDeleteButton.setAttribute('class', 'remove-this' )
    newDeleteButton.setAttribute('id', todoItem.todo_id)
    todoContainer.appendChild(newDeleteButton);
  })
}

var refresh = function() {
  todoContainer.innerHTML = ""
  createRequest('GET', url, {}, listCallback)
};

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
  console.log(id);
  createRequest('DELETE', url +'/' + id, undefined, refresh)
});

// completedContainer.addEventListener('click', function(e) {
//   var id = e.target.getAttribute("id");
//   var text = todoContainer.id.text
//   var completedTodo = JSON.stringify({"text": text , "completed": true});
//   createRequest('PUT', url +'/' + id, completedTodo, refresh)
// })
refresh()
