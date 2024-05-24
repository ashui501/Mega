from telegram import Update, constants, InlineKeyboardButton, InlineKeyboardMarkup

from info import dispatcher
from telegram.ext import CommandHandler, ContextTypes

from telegram.utils.helpers import mention_markdown

async def start(update: Update, context):

    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    mention = mention_markdown(user_id=user_id, name=user_name, version=2)

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
