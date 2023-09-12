#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv[2]; i++) {
    let line = '';
    for (let j = 0; j < argv[2]; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
