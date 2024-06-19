#!/usr/bin/node
let firstarg = process.argv[2];
if (firstarg !== undefined) {
	console.log(firstarg);
}else {
	console.log('No argument');
}
