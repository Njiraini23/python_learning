const numbers = [2, -30, 50, 20, -12, -9, 7];

const positiveSum = numbers
	.filter((number) => number > 0)
	.reduce((acc, cur) => acc + cur, 0);

console.log(positiveSum);
