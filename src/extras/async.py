"""
Asynchronously download a list of webpages and time it

Dependencies: Make sure you install aiohttp using: pip install aiohttp aiodns
"""
import asyncio
import aiohttp
from time import time

# Configuring logging to show timestamps
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

sites = [
    "http://news.ycombinator.com/",
    "https://www.yahoo.com/",
    "https://github.com/",
    "http://deelay.me/5000/http://deelay.me/",
]


async def find_size(session, url):
    log.info("START {}".format(url))
    async with session.get(url) as response:
        log.info("RESPONSE {}".format(url))
        page = await response.read()
        log.info("PAGE {}".format(url))
        return url, len(page)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for site in sites:
            tasks.append(find_size(session, site))
        results = await asyncio.gather(*tasks)
    for site, size in results:
        print("Read {:8d} chars from {}".format(size, site))


if __name__ == '__main__':
    start_time = time()
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
    print("Ran in {:6.3f} secs".format(time() - start_time))
