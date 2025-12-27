import time
import asyncio
import concurrent.futures


def func1():
    # 某個耗時操作
    time.sleep(2)
    return "SB"


async def main():
    loop = asyncio.get_running_loop()

    # 1. 在預設事件迴圈的 executor 中執行（預設為 ThreadPoolExecutor）
    # 第一步：內部會先呼叫 ThreadPoolExecutor 的 submit 方法，
    #         向執行緒池申請一個執行緒來執行 func1 函式，
    #         並回傳一個 concurrent.futures.Future 物件
    # 第二步：呼叫 asyncio.wrap_future，
    #         將 concurrent.futures.Future 物件包裝成 asyncio.Future 物件
    # 因為 concurrent.futures.Future 物件不支援 await 語法，
    # 所以必須包裝成 asyncio.Future 物件後才能使用
    fut = loop.run_in_executor(None, func1)
    result = await fut
    print('default thread pool', result)

    # 2. 在自訂的執行緒池中執行：
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, func1)
    #     print('custom thread pool', result)

    # 3. 在自訂的行程池中執行：
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, func1)
    #     print('custom process pool', result)


asyncio.run(main())