#!/usr/bin/node
const { argv } = require('process');

const firstValue = parseInt(argv[2], 10);

if (isNaN(firstValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstValue);
}
