#!/usr/bin/node

function factorial (x) {
    if (x === 1) {
      return (1);
    } else {
      return (x * factorial(x - 1))
    }
}

if (isNaN(process.argv[2])) {
  let result = factorial(1);
  console.log(result);
} else {
  let intgr = parseInt(process.argv[2]);
  let result = factorial(intgr);
  console.log(result)
}
