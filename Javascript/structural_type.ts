interface Point {
  x: number;
  y: number; 
}

function logPoint(p: point) {
  console.log(`${p.x}, ${p.y}`);
}

const point = { x: 12, y: 26 };
logPoint(point);
