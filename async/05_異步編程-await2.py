import asyncio


async def others():
    print("start")
    await asyncio.sleep(3)
    print("end")
    return "返回值"

async def func():
    print("執行協程函式內部程式碼")

    # 遇到 IO 操作會掛起(suspend)當前協程（任務），
    # 等 IO 操作完成後再繼續往下執行，
    # 當前協程掛起時，事件迴圈可以去執行其他協程（任務）。
    response = await others()

    print("IO 請求結果，結果為：", response)


asyncio.run(func())
