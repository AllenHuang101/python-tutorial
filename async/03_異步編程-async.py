import asyncio

async def func():
    print("Hello, World!")


result = func()

# 早期寫法
# loop = asyncio.get_event_loop()
# loop.run_until_complete(result)

# Python 3.7 以後新寫法
asyncio.run(result)
