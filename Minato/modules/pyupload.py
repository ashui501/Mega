import os
import time
import asyncio

OWNER_ID = 2107036689

from info import tbot 
from datetime import datetime
from Minato.events import register

path = TEMP_DOWNLOAD_DIRECTORY = "./"
water = "./Minato/resources/photo_2022-07-01_15-09-19.jpg"

client = tbot

@register(pattern=r"^/pyupload ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./Minato/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("**No File Found!**")
