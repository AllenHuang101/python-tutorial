import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

async def main():
    print("main 開始")

    # 建立 Task 列表
    task_list = [
        asyncio.create_task(func(), name="n1"),
        asyncio.create_task(func(), name="n2")
    ]

    print("main 結束")

    # 請事件迴圈幫我監控這些 Task，在它們完成之前先讓出控制權，等條件滿足後再回來。
    done, pending = await asyncio.wait(task_list)
    print(done)

asyncio.run(main())
