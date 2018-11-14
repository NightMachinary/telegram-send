#!/usr/bin/env python3
"""telegram-send
Usage:
  tsend.py <receiver> <message> [--file=<file>]
  tsend.py (-h | --help)
  tsend.py --version

Options:
  -f <file> --file=<file>   Sends a file, with message as its caption.
  -h --help     Show this screen.
  --version     Show version.

Examples:
  tsend.py some_friend "I love you ^_^" --file="~/pics/big_heart.png"

Created by Fereidoon Mehri. I release my contribution to this program to the public domain (CC0).
"""
from docopt import docopt
import asyncio
from telethon import TelegramClient, events

arguments = docopt(__doc__, version='telegram-send 0.1')

async def main():
    with open('./config') as f:
        api_id = f.readline()
        api_hash = f.readline()
        async with TelegramClient(
                    'alice_is_happy',
                    api_id,
                    api_hash) as client:
                # print(arguments)
                # if arguments['--file'] is not none:
                await client.send_message(arguments['<receiver>'], arguments['<message>'], file=arguments['--file'])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
