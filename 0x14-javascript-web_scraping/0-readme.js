#!/usr/bin/node
/*
 * A script that reads and prints
 * the content of a file
 */

let fs = require("fs");

if (!process.argv[2])
	process.exit();
fs.readFile(process.argv[1], 'utf8', (err, data) => {
	if (err)
		throw err;
	console.log(data.toString())
}
)
