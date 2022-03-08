#!/usr/bin/env python3

# A web socket server to receive VSS data for processing
#
# Copyright (C) 2021 Renesas Electronics Corporation
#

import asyncio
from websockets import serve
import json
from r_sim2vss_translater import translate
from iotdb_connector import vss_insert_aligned


# simple service configuration
ws_port = 8765
ws_host = None


async def handler(websocket):
    async for message in websocket:
        msg = json.loads(message)
        sim_payload = msg['arg']
        vss_data = translate(sim_payload)
        vss_insert_aligned(vss_data)


async def main():
    async with serve(handler, ws_host, ws_port):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())