import asyncio

async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")


async def main():
    # 取得目前的事件迴圈
    loop = asyncio.get_running_loop()

    # 建立一個任務（Future 物件），沒有綁定任何行為，這個任務永遠不知道什麼時候會結束。
    fut = loop.create_future()

    # 建立一個任務（Task 物件），綁定了 set_after 函式，
    # 函式內部會在 2 秒之後，替 fut 設定結果。
    # 也就是手動設定 Future 任務的最終結果，這樣 fut 就可以結束了。
    await loop.create_task(set_after(fut))

    # 等待 Future 物件取得最終結果，否則就會一直等待下去
    data = await fut
    print(data)


asyncio.run(main())
