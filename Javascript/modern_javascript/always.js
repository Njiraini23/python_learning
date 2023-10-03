const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 90, 9, 8, 7];
const evenNums = []
nums.forEach(num => {
	if (num % 2 === 0) {
		evenNums.push(num);
	}
});
console.log(evenNums);
