"""
1851_Event_Loop
"""

"""
response1 = request()
response2 = request()
response3 = request()
"""

import asyncio

async def request(number):
    print(f'request {number}')
    await asyncio.sleep(1)
    print(f'response {number}')
    
async def main():
    await asyncio.gather(request(1), request(2), request(3))

asyncio.run(main())