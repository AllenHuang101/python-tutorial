import asyncio

# await + 可等待對象(協成對象、任務對象、Future對象)
async def func():
    print("1. 開始執行 func")

    # 模擬 IO 操作
    # 事件循環會在此停下來，等待 await 後的可等待對象執行完成
    response = await asyncio.sleep(2)
    print("2. func 執行結束", response)

asyncio.run(func())
