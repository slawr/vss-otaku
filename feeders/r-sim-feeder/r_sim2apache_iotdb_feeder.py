#!/usr/bin/env python3

# A web socket server to receive VSS data for processing
#
# Copyright (C) 2021 Renesas Electronics Corporation
#

import asyncio
from websockets import serve
import json
import r_sim2vss_translater #import translate
import iotdb_connector


# simple websocket server service configuration
ws_port = 8765
ws_host = None


async def handler(websocket):
    # Connect to the IoTDB Server
    iotdb_connector.open_session()

    # Create TS schema
    # For this prototype we assume the schema already exists in the DB for the "normal" runtime case. Uncomment if you want feeder to create the schema
#    iotdb_connector.create_time_series()

    # Convert incoming sim data to VSS and write to DB
    async for message in websocket:
        msg = json.loads(message)
        sim_payload = msg['arg']
        vss_data = r_sim2vss_translater.translate(sim_payload)
        ts =  sim_payload['Timestamp']
        iotdb_connector.insert_vss_ts(ts, vss_data)

    # Close connection
    iotdb_connector.close_session()


async def main():
    async with serve(handler, ws_host, ws_port):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())