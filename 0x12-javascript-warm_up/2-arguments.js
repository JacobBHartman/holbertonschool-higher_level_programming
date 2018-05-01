#!/usr/bin/node

if (process.argv[2] && process.argv[3] == null) {
  console.log('No argument')
} else if (process.argv[3] && process.argv[4] === 'undefined') {
  console.log('Argument found')
} else {
  console.log('Arguments found')
}
