#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 4) {
    console.log(0);
} else {
    let array = argv;
    array.splice(0, 2);
    for (let i = 0; i < array.length; i++) {
      array[i] = parseInt(array[i]);
    }
    console.log(array)
    array.sort((a, b) => { return a - b });
    console.log(array)
}
