import asyncio
# from asyncio import Queue
#
# async def left():
#     for i in range(5):
#         print('LEFT')
#         await asyncio.sleep(1)
#
# async def worker(q):
#     for i in range(5):
#         await asyncio.sleep(1)
#         await q.put(f'%{i}')
#
#
# async def test(q):
#     for i in range(5):
#         print(await q.get())
#
# q = Queue()
# asyncio.get_event_loop().run_until_complete(asyncio.gather(test(q), worker(q), left()))

# import aioredis
# import asyncio
#
#
# async def main():
#     conn = await aioredis.create_redis('redis://localhost')
#     await conn.zadd('group', 60, '1')
#     await conn.zadd('group', 60, '2')
#     await conn.xadd()
#     # print(await conn.brpop('test'))
#
# asyncio.get_event_loop().run_until_complete(main())

