import asyncio


async def test(q, i):
    print(i)
    if i == 10:
        # await q.put('END')
        pass
    else:
        await asyncio.sleep(3)
async def wait_():
    for i in range(1):
        print('wait')
        await asyncio.sleep(0.1)


async def main():
    q = asyncio.queues.Queue()

    f, p = await asyncio.wait([test(q, c) for c in range(11)], timeout=1)
    print(f, '\n', p)


    # print
    # asyncio.ensure_future(wait_())
    # print(await q.get())
    # print(worker)

asyncio.get_event_loop().run_until_complete(main())
