# WS server example
import asyncio
import websockets
import locationlogger

def saveMessage(message):
    locationlogger.log(message)

async def handler(websocket, path):
    remote_ip = websocket.remote_address[0]
    message = await websocket.recv()

    saveMessage(message)

    print(f"({remote_ip}) wrote: {message}")
        
start_server = websockets.serve(handler, "localhost", 4444)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()