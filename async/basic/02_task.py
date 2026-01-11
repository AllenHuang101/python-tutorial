import asyncio
import time


async def call_api(name: str, delay: float):
    print(f"{name} - step 1")
    # 模擬 IO 操作的等待時間
    await asyncio.sleep(delay)
    print(f"{name} - step 2")


async def main():
    time_1 = time.perf_counter()

    print("start A coroutine")
    await call_api("A", 3)
    print("finished A coroutine")

    print("start B coroutine")
    await call_api("B", 3)
    print("finished B coroutine")

    time_2 = time.perf_counter()
    print(f"Total time: {time_2 - time_1} seconds")


asyncio.run(main())
