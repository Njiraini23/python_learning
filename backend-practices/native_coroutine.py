import asyncio

@asyncio.coroutine
def py34_coro():
    """Generates a coroutine"""
    yield from stuff():
        await stuff()
