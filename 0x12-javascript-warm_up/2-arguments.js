#!/usr/bin/node
let numargs = process.argv.length;
if (numargs === 2) {
    console.log('No argument');
} else if (numargs === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
