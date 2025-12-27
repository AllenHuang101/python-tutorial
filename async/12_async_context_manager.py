import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("🔌 建立非同步資源")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("🔒 釋放非同步資源")
        await asyncio.sleep(1)

    async def do_something(self):
        print("⚙️ 執行非同步操作")
        await asyncio.sleep(1)
        return 666


async def main():
    async with AsyncContextManager() as mgr:
        result = await mgr.do_something()
        print("結果:", result)

asyncio.run(main())
