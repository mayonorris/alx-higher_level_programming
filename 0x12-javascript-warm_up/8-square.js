#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (!isNaN(size) && size > 0) {
    for (let i = 0; i < size; i++) {
        console.log('X'.repeat(size));
    }
} else {
	if (size < 0)
{
        console.log('')
} else{
    console.log("Missing size");
}
}
