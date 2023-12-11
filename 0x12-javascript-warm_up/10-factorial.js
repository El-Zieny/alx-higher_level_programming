#!/usr/bin/node
const { argv } = require('process');
function factorial (i) {
    if (i === 1) { return 1; }
    return i * factorial(i - 1);
}
const x = parseInt(argv[2]);
if (isNaN(x)) {
    console.log(1);
} else {
    console.log(factorial(x));
}
