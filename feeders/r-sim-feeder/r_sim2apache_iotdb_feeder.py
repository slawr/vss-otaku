#!/usr/bin/env python3

# A web socket server to receive VSS data for processing
#
# Copyright (C) 2021 Renesas Electronics Corporation
#

import asyncio
from websockets import serve
import json
from r_sim2vss_translater import translate


# simple service configuration
ws_port = 8765
ws_ip = 'localhost'


async def handler(websocket):
    async for message in websocket:
        msg = json.loads(message)
        sim_payload = msg['arg']


async def main():
    async with serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())