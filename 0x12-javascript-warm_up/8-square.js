#!/usr/bin/node
const { argv } = require('process');

const size = parseInt(argv[2], 10);

if (isNaN(size)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < size; i += 1) {
    console.log('x'.repeat(size));
  }
}
