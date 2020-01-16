import asyncio

import aiohttp
from codetiming import Timer


async def task(name, work_queue):
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            print(f'Task {name} getting URL: {url}')
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()


async def main():
    work_queue = asyncio.Queue()

    for url in [
        'https://google.com',
        'https://yahoo.com',
        'https://linkedin.com',
        'https://apple.com',
        'https://microsoft.com',
        'https://facebook.com',
        'https://twitter.com',
    ]:
        await work_queue.put(url)

    with Timer(text='\nTotal elapsed time: {:.1f}'):
        await asyncio.gather(
            asyncio.create_task(task('One', work_queue)),
            asyncio.create_task(task('Two', work_queue)),
        )


if __name__ == '__main__':
    asyncio.run(main())
