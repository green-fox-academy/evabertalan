"use-strict"

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'todo'
});

connection.connect();

var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

function getItem(todo_id, callback) {
  connection.query('SELECT text, completed, status FROM new_table WHERE todo_id=?', todo_id,
    function(err, result){
    if (err) {throw err;}
    console.log(result);
    callback(result);
  });
}

function addItem(attributes) {
  connection.query('INSERT INTO new_table SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function removeItem(todo_id, callback) {
  connection.query('DELETE FROM new_table WHERE todo_id=?', todo_id, function(err, result){
     if (err) throw err;
     console.log(result.insertId);
     callback(result);
   });
}

function completeItems(todo_id, callback) {
console.log(todo_id,'ez');
  connection.query('UPDATE new_table SET status="completed" WHERE todo_id=?', todo_id, function(err, result) {
    if (err) throw err;
    console.log(result);
    callback(result);
  });
}

function allItems(callback) {
  connection.query('SELECT * FROM new_table', function(err, results) {
    if (err) throw err;
    callback(results);
  });
}


module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
  update: completeItems
};
