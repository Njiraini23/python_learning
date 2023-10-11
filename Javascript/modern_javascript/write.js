const { readFile, writeFile } = require('fs')

readFile('./file.js', 'utf8', (err, result) => {
	if (err) {
		console.log(err)
		return
	}
	const first = result
	readFile('./file.js', 'utf8', (err, result) => {
		if (err) {
			console.log(err)
			return
		}
		console.log(result)
	})
});
