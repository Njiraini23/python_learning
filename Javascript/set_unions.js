function union(setA, setB) {
  const _union = new Set(SetA);
  for (const elem of setB) {
    _union.add(elem);
  }
  return _union;
}
