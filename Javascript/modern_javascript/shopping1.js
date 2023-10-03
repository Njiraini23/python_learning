const cart = [
	{ id: 1, name: 'Product 1', price: 130 },
	{ id: 2, name: 'Product 2', price: 150 },
	{ id: 3, name: 'Product 3', price: 175 },
];

const totals = cart.reduce(function (acc, product) {
	return acc + product.price;
}, 0);

console.log(totals)
