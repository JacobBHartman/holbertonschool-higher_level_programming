#!/usr/bin/node

if (isNaN(parseInt(process.argv[2])) || isNaN(parseInt(process.argv[3]))) {
  console.log('NaN');
} else {
  let a = parseInt(process.argv[2]);
  let b = parseInt(process.argv[3]);
  add(a, b);
}

function add (a, b) {
  console.log(a + b);
}
