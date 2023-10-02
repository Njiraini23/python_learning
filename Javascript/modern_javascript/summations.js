function sum(...numbers) {
	let totals = 0;
	for (const num of numbers) {
		totals += num;
	}
	return totals;
}
console.log(sum(1, 2, 3, 4, 5, 6, 7, 8))
