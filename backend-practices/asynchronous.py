async def g():
    #pause here and come back to g() when f() is ready
    r = await f()
    return r
