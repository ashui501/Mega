import sys
import requests
import io
import time
import traceback
from requests import post
from subprocess import getoutput as run
from datetime import datetime

from pyrogram import filters, Client 
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from info import DEV_USERS, ADMINS, OWNER_ID

dev_users = DEV_USERS
DEVS = ADMINS
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@Client.on_message(filters.command('devlist'))
def devlist(_, m):
    if str(m.from_user.id) in DEV_USERS:
        m.reply(str(DEV_USERS))
    else:
        m.reply("only Devs can access this command!")
        
@Client.on_message(filters.user(ADMINS) & filters.command("sh", prefixes=['/', '.', '?', '-']))
def sh(_, m):
    if m.from_user.id in ADMINS:
        code = m.text.replace(m.text.split(" ")[0], "")
        x = run(code)
        m.reply(
            f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")
    else:
        m.reply("only Devs can access this command!")

def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@Client.on_message(filters.command(["getsudos","sudolist"]))
async def sudolist(_, message):
           if message.from_user.id not in dev_user or not message.from_user.id in (await get_sudoers()):
                 return await message.reply("**Only Rank Users Can Access**")
           else:
                  user_ids = (await get_sudoers())
                  sudo_text = ""
                  for name in user_ids:
                           ok = await bot.get_users(user_ids)
                           sudo_text = f"**• {ok.mention}**"
                  await message.reply(sudo_text)

@Client.on_message(
    filters.command("logs", prefixes=[".", "/", ";", "," "*"]) & filters.user(ADMINS)
)
def sendlogs(_, m: Message):
    logs = run("tail logs.txt")
    x = paste(logs)
    keyb = [
        [
            InlineKeyboardButton("Link", url=x),
            InlineKeyboardButton("File", callback_data="sendfile"),
        ],
    ]
    m.reply(x, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(keyb))

@Client.on_message(filters.command(["run","eval", "e"]))
async def eval(client, message):
    if not message.from_user.id in DEVS:
         return await message.reply_text("You Don't Have Enough Rights To Run This!")
    if len(message.text.split()) <2:
          return await message.reply_text("Input Not Found!")
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(None, 1)[1]
    start = datetime.now()
    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    end = datetime.now()
    ping = (end-start).microseconds / 1000
    final_output = "📎 Input: "
    final_output += f"{cmd}\n\n"
    final_output += "📒 Output:\n"
    final_output += f"{evaluation.strip()} \n\n"
    final_output += f"✨ Taken Time: {ping}ms"
    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await status_message.edit_text(final_output)
        
@Client.on_message(filters.command("ud"))
async def ud(_, message: Message):
       ud = await message.reply_text("finding.. define.")
       if len(message.command) < 2:
           return await ud.edit("» Give some text")
       text = message.text.split(None, 1)[1]
       results = requests.get(
           f'https://api.urbandictionary.com/v0/define?term={text}'
       ).json()
       try:
           reply_text = f'**results: {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
       except:
           reply_text = 'Nothing found :('
       await ud.edit(reply_text)

def get_readable_time2(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d", "w", "m", "y"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
