dataset = {data for line in aiter()
        async for data in line
        if check(data)}
