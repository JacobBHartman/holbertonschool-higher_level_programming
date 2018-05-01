#!/usr/bin/node

if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log('0');
} else {
  let idx = 2;
  let max = -Infinity;
  while (process.argv[idx] !== undefined) {
    if (process.argv[idx] > max) {
      max = process.argv[idx];
    }
    idx++;
  }

  let idx2 = 2;
  let max2 = -Infinity;
  while (process.argv[idx2] !== undefined) {
    if (process.argv[idx2] > max2 && process.argv[idx2] !== max) {
      max2 = process.argv[idx2];
    }
    idx2++;
  }

  console.log(max2);
}
