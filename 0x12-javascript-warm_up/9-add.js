#!/usr/bin/node
const { argv } = require('process');
function add(a, b) {
    return a + b;
}
const x = parseInt(argv[2]);
const z = parseInt(argv[3]);
if (isNaN(x) || isNaN(z)) {
    console.log(NaN);
} else {
    console.log(add(x, z));
}
