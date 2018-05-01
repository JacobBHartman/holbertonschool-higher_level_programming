#!/usr/bin/node

if (typeof process.argv[2] === 'undefined') {
  console.log('No argument');
} else if (typeof process.argv[3] === 'undefined') {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
