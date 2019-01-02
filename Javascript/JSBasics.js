// declaring vars
const firstName = 'Mich';
// no diff in single/ double quotes
// semi colons optional

const val = 42
// no need to declare type

const arr = [
  'str',
  42,
  function() {console.log('hi')}
]
// doesn't matter what you toss into array
// can have trailing commas

const imp = val + ''

console.log(typeof imp)
// type of ^

arr[2]()

for (let i = 0; i < arr.length; i++){
  console.log(arr[i])
}

// objects

const me = new Object()
me.firstName = "Michelle"
me.greet = function(){
  consle.log('hi')
}

// object literal

const me2 = {}
me2['firstName'] = 'Mich'
const key = 'age'
me2[key] = 19

// inline
const me3 = {
  firstName: 'Miche',
  loc: {
    now: 'Vietnam',
    home: 'Malaysia'
  }
}

console.log(me3.loc)
console.log(me['firstName'])
// all keys auto cast to string
// use bracket notation for retrieving when you have dynamic key, else convention is dot

// object mutation
const test1 = {
  att1: 1,
  att2: 2
}

const test2 = test1

// objects store things as references, so both test1 and test2 have different references, but store the same references (attributes)
// updating the attribute of one updates the other

// if you want to copy an object but have diff att references
const test3 = Object.assign({}, test1)

test2.att1 = 3

console.log(test1)
console.log(test3)


/* Learning Javascript

// Function forms

// declaration
function test(num){
  return(`declaration ${num}`);
}

// expression

const test1 = function(num) {
  return(`expression ${num}`);
};

// expression w arrow function syntax

const test2 = (num) => {
  return(`expression w arrow syntax ${num}`);
};

// concise body

const test3 = num = `expression w arrow syntax ${num}`;

console.log(test(num));
console.log(test1(num));
console.log(test2(num));
console.log(test3(num));
*/
