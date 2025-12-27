import asyncio

async def calculate(x: int, y: int) -> int:
    res = x + y
    print(res)
    return res

# coroutine object
# o = calculate(1, 2)

async def main():
    print("main start")
    # 執行 coroutine 物件
    await calculate(1, 2)
    print("main end")

# asyncio.run() 啟動事件循環，並且把 coroutine 物件丟到事件循環中執行。
asyncio.run(main())

