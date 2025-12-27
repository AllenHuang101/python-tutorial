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
        await asyncio.wait_for(task, timeout=2)
    except TimeoutError:
        print("Timeout")
        await task

async def my_timeout():
    task = asyncio.create_task(play_music("一路向北"))

    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=2)
    except TimeoutError:
        print("Timeout")

async def my_gather():
    result = await asyncio.gather(play_music("一路向北"), play_music("告白氣球"))
    print(result)

async def my_gather_with_exception():
    result = await asyncio.gather(play_music("一路向北"), play_music("告白氣球"), call_api(), return_exceptions=True)
    print(result)
   
if __name__ == "__main__":
    # asyncio.run(my_cancel())
    # asyncio.run(my_cancel_with_timeout())
    # asyncio.run(my_timeout())
    # asyncio.run(my_gather())
    asyncio.run(my_gather_with_exception())
    
