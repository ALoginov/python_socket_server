# WS client example

import asyncio
import websockets

async def hello():
    uri = "localhost:4444"
    async with websockets.connect(uri) as websocket:
        print('Start messaging')
        name = input()

        await websocket.send(name)
        print(f"> {name}")

asyncio.get_event_loop().run_until_complete(hello())