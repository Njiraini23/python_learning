const numbers = [2, 3, 4, 5, 6, 7, 8, 9];

const squareAndDouble = numbers
  .map((number) => Math.sqrt(number))
  .map((sqrt) => sqrt * 2);

console.log(squareAndDouble);
