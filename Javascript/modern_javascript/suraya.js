const names = ['ken', 'symo', 'sam', 'kim', 'pato'];

const cNames = names.map((name) => {
  return name[0].toUpperCase() + name.slice(1, name.length);
});

console.log(cNames);
