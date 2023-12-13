#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  let length = list.length - 1;
  for (let i = 0; length + 1; i++, length--) {
    reversed[i] = list[length];
  }
  return reversed;
};
