#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
