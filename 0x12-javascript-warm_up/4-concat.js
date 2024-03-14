#!/usr/bin/node
const firstArg = process.argv[2];
const secondArg = process.argv[3];
if (firstArg !== undefined && secondArg !== undefined) {
    console.log(`${firstArg} is ${secondArg}`);
} else {
    console.log("undefined is undefined");
}
