import asyncio
import time

async def call_api(name: str, delay: float):
    print(f"{name} - step 1")
    await asyncio.sleep(delay)
    print(f"{name} - step 2")


async def main():
    time_1 = time.perf_counter()

    print("start A coroutine")
    # 創建協程放到事件循環中
    task_1 = asyncio.create_task(call_api("A", 2))

    print("start B coroutine")
    # 創建協程放到事件循環中
    task_2 = asyncio.create_task(call_api("B", 3))

    await task_1
    print("task 1 completed")
    await task_2
    print("task 2 completed")
    time_2 = time.perf_counter()

    print(f"Total time: {time_2 - time_1} seconds")

asyncio.run(main())