const library = [
	{
		title: 'The Dark Knight',
		author: 'Jack Daniels',
		status: {
			own: true,
			reading: false,
			read: false
		},

	},
	{
		title: 'The mystery ride',
		author: 'Kelvin Little',
		status: {
			own: true,
			reading: false,
			read: false
		},
	},
	{
		title: 'My Altar is Calling',
		author: 'David Dam',
		status: {
			own: true,
			reading: false,
			read: false,
		},
	},
];

library[0].status = true;
library[1].status = true;
library[2].status = true;

// Step 3 Destructuring
const { title: firstBook } = library[0];
console.log(firstBook);

// step 4
str = JSON.stringify(library);

console.log(str)
