const myMap = new Map();
myMap.set(0, "Zero");
myMap.set(1, "One");

for (const [key, value] of myMap) {
  console.log(`${key} = ${value}`);
}

for (const value of myMap.values()) {
  console.log(value);
}
