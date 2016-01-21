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

function getItem(id) {
  return items[id];
}

function addItem(attributes) {
  connection.query('INSERT INTO new_table SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function removeItem(id) {
  connection.query('INSERT INTO new_table SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

// delete items[id];


function allItems(cb) {
  connection.query('SELECT * FROM new_table', function(err, results) {
    if (err) throw err;
    cb(results);
  });
}


module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
};
