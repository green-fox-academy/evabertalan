'use strict';


var student = {
  age: 10,
  sayYourAge: sayYourAge
};

function sayYourAge() {
  console.log('I am ' + this.age);
}

student.sayYourAge();

//sayYourAge(); csak akkor dob hibat ha van ude strict , ha nincs ez undefined (a this undefined) miatt

/*var func = student.sayYourAge();
func()
nem hivhato meg, mert nincs itt athis */
