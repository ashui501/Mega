import asyncio

from pyrogram import filters
from pyrogram.raw import functions
from pyrogram.types import Message

from info import Jiraiya as UserBot


@UserBot.on_message(filters.command(["screenshot", "ss"]))
async def screenshot(bot: UserBot, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.invoke(
            functions.messages.SendScreenshotNotification(
                peer=await UserBot.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=UserBot.rnd_id(),
            )
        ),
    )


