#!/usr/bin/env python3

# A web socket server to receive VSS data for processing.
#
# Processing of the data is deliberately missing so this
# can quickly be copied as a template or starting point
# for new work.
#
# Copyright (C) 2021 Renesas Electronics Corporation
#

import asyncio
from websockets import serve
import json

# simple service configuration
ws_port = 8765
ws_host = None


async def handler(websocket):
    async for message in websocket:
        msg = json.loads(message)
        sim_payload = msg['arg']
#       Do some processing

async def main():
    async with serve(handler, ws_host, ws_port):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())