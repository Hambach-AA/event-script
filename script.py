import asyncio
import websockets
import json
import requests
async def event():
    uri = "ws://miac74.ru:9998"
    async with websockets.connect(uri) as websocket:
        index=0
        while True:
          if index < 1000:
            greeting = await websocket.recv()
            file = open("text.txt","r")
            buf = json.load(file)
            buf.append(greeting)
            file.close()
            file = open("text.txt","w")
            json.dump(buf,file)
            file.close()
            index=index+1
          else:
            file = open("text.txt","r")
            buf = json.load(file)
            file.close()
            requests.post(url, json=json.dump(buf))
            file = open("text.txt","w")
            json.dump(add,file)
            file.close()
            index=0
add=[]
file = open("text.txt","w")
json.dump(add,file)
file.close()
asyncio.get_event_loop().run_until_complete(event())
