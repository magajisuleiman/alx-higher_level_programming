#!/usr/bin/node
const { argv } = require('process');

// factorial
// of a number 5 = (5*4*3*2*1)
// and 1 factoria is 1

const n = parseInt(argv[2], 10);

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    if (n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
}
console.log(factorial(n));
