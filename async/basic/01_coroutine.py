import asyncio


# 定義協程 coroutine 函式
async def calculate(x: int, y: int) -> int:
    res = x + y
    print(res)
    return res


# 產生 coroutine 對象
# o = calculate(1, 2)
# 把協程對象丟到事件循環中執
asyncio.run(calculate(1, 2))


async def main():
    print("main start")
    # 協程內部又去執行另一個協程
    # main 進入等待狀態
    await calculate(1, 2)
    print("main end")


# asyncio.run() 啟動事件循環，並且把 coroutine 物件丟到事件循環中執行。
asyncio.run(main())
