'use strict';

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'test',
  password: '1234',
  database: 'todo'
});

connection.connect();

function addUser(attributes) {
  // var sql = "INSERT INTO new_table SET text='hello', status='new'"
  connection.query('INSERT INTO user SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  })
}

function getUser() {
  connection.query()
}

function updateUser(attributes) {
  connection.query('UPDATE user SET ?', attributes, function(err, result) {

  })
}

module.exports = {
  add: addUser,
  get: getUser,
  getUserById: getUserById
};
