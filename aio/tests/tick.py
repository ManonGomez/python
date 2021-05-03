import aiohttp
import asyncio
from rich import print

async def main():

   async with aiohttp.ClientSession() as session:
        async with session.get('http://51.15.17.205:9000/tick/ManonGomez') as resp:
            print(resp.status)
            print(await resp.json())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())