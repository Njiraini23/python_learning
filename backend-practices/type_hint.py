from typing import Generator

def generate() -> Generator[int, None, None]:
    for i in range(10):
        yield i

for i in generate():
    print (i)
