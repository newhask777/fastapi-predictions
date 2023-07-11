
import asyncio
from websockets.sync.client import connect

def hello():
    with connect("wss://ws.sofascore.com:9222/") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

while True:
    hello()


