import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

async def main():
    print("main 開始")

    # 建立 Task 物件，將當前執行的 func 函式任務加入事件迴圈
    task1 = asyncio.create_task(func())
    
    # 建立 Task 物件，將當前執行的 func 函式任務加入事件迴圈
    task2 = asyncio.create_task(func())

    print("main 結束")

    # 當協程執行到 IO 操作時，會自動切換去執行其他任務
    # 此處的 await 是等待對應的協程全部執行完成並取得結果
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)

asyncio.run(main())
