import asyncio
import aiohttp

async def fetch(session, url):
    print("發送請求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('_')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)
    print("下載完成：", url)

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFOCsRnzU621.jpg',
            'https://www3.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChsCSv2B1CAuntfAADjFd6800429.jpg',
            'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCMATOB3AAGG7VKosGY193.jpg'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())