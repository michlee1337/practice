// Learning Javascript

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
