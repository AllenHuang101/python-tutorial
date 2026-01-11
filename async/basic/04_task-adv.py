from colorama import Fore, init

init(autoreset=True)

import asyncio


async def play_music(music: str):
    print(f"Start playing: {music}")
    await asyncio.sleep(5)
    print(f"Finished playing: {music}")

    return music


async def call_api():
    print("Calling API...")
    raise Exception("API call failed")


async def my_cancel():
    task = asyncio.create_task(play_music("一路向北"))

    await asyncio.sleep(3)

    if not task.done():
        task.cancel()


async def my_cancel_with_timeout():
    task = asyncio.create_task(play_music("一路向北"))

    try:
        # 任務執行超過 2 秒就取消
        await asyncio.wait_for(task, timeout=2)
    except TimeoutError:
        print("Timeout")
        await task


async def my_timeout():
    task = asyncio.create_task(play_music("一路向北"))

    try:
        # 任務超過超時會拋出異常，但任務不會被取消
        await asyncio.wait_for(asyncio.shield(task), timeout=2)
    except TimeoutError:
        print("Timeout")


async def my_gather():
    print(f"{Fore.RED} 同時執行多個任務，並且等待所有任務完成...")
    # 同時執行多個任務，並且等待所有任務完成
    # 不用一個一個創建 Task，然後一個一個 await
    result = await asyncio.gather(play_music("一路向北"), play_music("告白氣球"))
    print(result)


async def my_gather_with_exception():
    print(f"{Fore.RED} 同時執行多個任務，發生異常不要中斷...")
    # 協程可能發生異常，希望發生異常時不要中斷並取得異常結果
    result = await asyncio.gather(
        play_music("一路向北"),
        play_music("告白氣球"),
        call_api(),
        return_exceptions=True,
    )
    print(result)


if __name__ == "__main__":
    # asyncio.run(my_cancel())
    # asyncio.run(my_cancel_with_timeout())
    # asyncio.run(my_timeout())
    asyncio.run(my_gather())
    asyncio.run(my_gather_with_exception())
