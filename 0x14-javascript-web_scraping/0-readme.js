#!/usr/bin/node
/*
 * A script that reads and prints
 * the content of a file
 */

let fs = require("fs");

if (!process.argv[2])
	process.exit();
fs.readFile(process.argv[2], 'utf8', (err, data) => {
	if (err)
		console.log(err);
	else
		console.log(data.toString());
}
)
