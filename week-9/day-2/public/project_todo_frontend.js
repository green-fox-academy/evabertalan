'use strict';

var url = 'http://localhost:3000/todos';
var todoContainer = document.querySelector('.todo-container')
// var todoRow = document.querySelector('.todo-row')
var todoInput = document.querySelector('.todo-input')
var addTodo = document.querySelector('.add-todo')

var completeTodo = document.querySelector('.complete')
var removeTodo = document.querySelector('.remove')

var completeElement = document.querySelector('.completed-todo')

var listCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(todoItem) {
    var newTodoRow = document.createElement('tr');
    newTodoRow.setAttribute('class', 'todo-row' )
    todoContainer.appendChild(newTodoRow);

    // var newCompletedButton = document.createElement('td')
    // newCompletedButton.innerText = 'Complete'
    // newCompletedButton.setAttribute('class', 'complete' )
    // newCompletedButton.setAttribute('id', todoItem.todo_id)
    // newTodoRow.appendChild(newCompletedButton);

    var newCheckbox = document.createElement('INPUT');
    newCheckbox.setAttribute('type', 'checkbox');
    newCheckbox.setAttribute('id', todoItem.todo_id);
    newCheckbox.setAttribute('class','checkbox');
    newTodoRow.appendChild(newCheckbox);

    var newTodoItem = document.createElement('td');
    newTodoItem.setAttribute('id', todoItem.todo_id)
    newTodoItem.innerText = todoItem.text;
    newTodoRow.appendChild(newTodoItem);



    var newDeleteButton = document.createElement('td')
    newDeleteButton.innerText = 'Remove'
    newDeleteButton.setAttribute('class', 'remove' )
    newDeleteButton.setAttribute('id', todoItem.todo_id)
    newTodoRow.appendChild(newDeleteButton);
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


var removeElement = document.querySelector('.todo-container');
// var removeElement = document.querySelector('.remove');
console.log(removeElement);
removeElement.addEventListener('dblclick', function(e) {
  var id = e.target.getAttribute("id");
  console.log(id);
  createRequest('DELETE', url +'/' + id, undefined, refresh)
});

completeElement.addEventListener('click', function() {
  var done = document.querySelectorAll('.checkbox');
  for (var i = 0; i < done.length; i++){
    if (done[i].checked === true) {
      // document.body.style.backgroundColor = "red";
      document.body.style.backgroundColor = "red";
      console.log(done[i]);
      console.log("kaka");
    }
  }
});




// var completeElement = document.querySelector('.todo-container')
// // console.log(completeElement);
// completeElement.addEventListener('click', function(e) {
//   var id = e.target.getAttribute("id");
//   var completedTodo = JSON.stringify({completed: true});
//   // var createTodoCallback = function (response) {
//   //   refresh();
//   // }
//   createRequest('PUT', url +'/' + id, completeTodo, refresh)
// })
refresh()
