#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i <= argv[2]; i++) {
    console.log('C is fun');
  }
}
