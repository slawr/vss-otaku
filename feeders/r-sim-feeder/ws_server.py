#!/usr/bin/env python3

# A web socket server to receive VSS data for processing
#
# Copyright (C) 2021 Renesas Electronics Corporation
#

import asyncio
from websockets import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())