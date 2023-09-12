#!/usr/bin/node
const { argv } = require('process');

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
