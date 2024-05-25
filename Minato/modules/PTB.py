

# nandha/plugins/main.py


from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, __version__ as ptbver
from telegram.ext import CommandHandler, CallbackContext
from telegram.utils.helpers import mention_html
from info import dispatcher as app

import html
import sys

def start(update: Update, context: CallbackContext):

    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    mention = mention_html(user_id, html.escape(user_name))

    keyboard = [
        [
            InlineKeyboardButton("Group 🌟", url="NandhaChat.t.me"),
            InlineKeyboardButton("Channel 🌟", url="NandhaBots.t.me"),
        ],
        [
            InlineKeyboardButton("💀 Nandha 💀", url=f"tg://user?id=5696053228")
        ]
    ]

    buttons = InlineKeyboardMarkup(keyboard)
    python_version = sys.version_info
    pyver = '{}.{}.{}'.format(python_version.major, python_version.minor, python_version.micro)
    ptb = "<a href='https://docs.python-telegram-bot.org'>Python-Telegram-Bot</a>"
    
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"<b>Hello there {mention}, I'm Simple bot made by @NandhaBots using {ptb} Library.\n\n➲ Python Telegram Bot: <code>{ptbver}</code>\n➲ Python: <code>{pyver}</code></b>",
        parse_mode=ParseMode.HTML,
        reply_markup=buttons
    )

start_handler = CommandHandler('start', start)
app.add_handler(start_handler)
