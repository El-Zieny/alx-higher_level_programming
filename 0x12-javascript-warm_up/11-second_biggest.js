#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 4) {
  console.log(0);
} else {
  const array = argv;
  array.splice(0, 2);
  for (let i = 0; i < array.length; i++) {
    array[i] = parseInt(array[i]);
  }
  array.sort((a, b) => { return a - b; });
  array.reverse();
  for (let i = 0; i < array.length; i++) {
    if (array[0] === array[1]) {
      array.shift();
    }
  }
  console.log(array[1]);
}
