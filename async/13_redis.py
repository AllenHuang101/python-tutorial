import asyncio
import aioredis


async def execute(address, password):
    print("開始執行", address)

    # 網路 IO 操作：先連線到 47.93.4.197:6379，
    # 當遇到 IO 時會自動切換任務，轉而去連線 47.93.4.198:6379
    redis = await aioredis.create_redis_pool(address, password=password)

    # 網路 IO 操作：遇到 IO 時會自動切換任務
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 網路 IO 操作：遇到 IO 時會自動切換任務
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    redis.close()
    # 網路 IO 操作：遇到 IO 時會自動切換任務
    await redis.wait_closed()

    print("結束", address)


task_list = [
    execute('redis://xxx:6379', "xxx"),
    execute('redis://xxx:6379', "xxx")
]

asyncio.run(asyncio.wait(task_list))
