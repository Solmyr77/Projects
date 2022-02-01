import asyncio

q = asyncio.Queue()

async def loop_a(q):
  for _ in range(10):
    value = await q.get()
    print(value)

async def loop_b(q):
  for _ in range(10):
    await q.put("a")
    print("b")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(loop_a(q), loop_b(q)))