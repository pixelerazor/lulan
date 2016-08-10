#!/usr/bin/python3

from datetime import tzinfo, timedelta, datetime
import asyncio
import websockets
import time

minDelay = 60;
class TZ(tzinfo):
    def utcoffset(self, dt): return timedelta(minutes=minDelay)

class Chat:
    def __init__(self):
        self.messages = []
        self.num = 0

    def addMessage(self, message):
        spl = message.split(",")
        current = time.gmtime()
        timeString = datetime(current.tm_year, current.tm_mon, current.tm_mday, current.tm_hour, current.tm_min, current.tm_sec, 0, tzinfo=TZ()).isoformat(" ")
        self.messages.insert(0, (timeString, spl[0], spl[1]))
        self.num += 1

MyChat = Chat()

async def messages(websocket, path):
    num = 0
    while True:
        if num != MyChat.num:
            num = MyChat.num
            mess = ""
            for i in MyChat.messages:
                newMessage = str(i[0])+","+str(i[1])+","+str(i[2])+";"
                mess += newMessage
            print(mess[:-1])
            await websocket.send(mess[:-1])
        await asyncio.sleep(1)

async def receive(websocket, path):
    while True:
        message = await websocket.recv()
        MyChat.addMessage(message)
        print("< {}".format(message))

start_server = websockets.serve(receive, '127.0.0.1', 8001)
start_server2 = websockets.serve(messages, '127.0.0.1', 8002)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(start_server2)
asyncio.get_event_loop().run_forever()
