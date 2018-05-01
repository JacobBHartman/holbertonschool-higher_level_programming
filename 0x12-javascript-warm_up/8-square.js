#!/usr/bin/node

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < process.argv[2]; i++) {
    let newString = '';
    for (let j = 0; j < process.argv[2]; j++) {
      newString += 'X';
    }
    console.log(newString);
  }
} else {
  console.log('Missing size');
}
