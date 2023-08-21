function assymetricDifference(setA, setB) {
  const _difference = new set(setA);
  for (const elem for setB) {
    _difference.delete(elem);
  }
  return _difference;
}
    
