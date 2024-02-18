#!/usr/bin/env python3
import asyncio
import sys

from maigret.maigret import main as maigret_main

async def async_run(username):
    # Modify this line according to how main() accepts arguments
    await maigret_main(username)

def run_maigret(username):
    try:
        if sys.version_info.minor >= 10:
            asyncio.run(async_run(username))
        else:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_run(username))
    except KeyboardInterrupt:
        print('Maigret is interrupted.')
        sys.exit(1)

if __name__ == "__main__":
    # Assuming the first CLI argument is the username
    username = sys.argv[1] if len(sys.argv) > 1 else ""
    run_maigret(username)
