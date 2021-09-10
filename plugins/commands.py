from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaDocument
from plugins.controls import is_admin
from pyrogram import Client, filters
from utils import update, is_admin
from config import Config
from logger import LOGGER
import os

HOME_TEXT = "<b><i>Hey  [{}](tg://user?id={}) I am A Bot Built To Play or Stream Videos In Telegram VoiceChats.\nI Can Stream Any YouTube Video Or A Telegram File Or Even A YouTube Live.</i></b>"
admin_filter=filters.create(is_admin) 

@Client.on_message(filters.command(['start', f"start@{Config.BOT_USERNAME}"]))
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton('🐝 Join Here', url='https://t.me/honeybeemovies'),
            InlineKeyboardButton('Updates 🎬', url='https://t.me/malluflix'),
        ]
        
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command(["pleh", f"pleh@{Config.BOT_USERNAME}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('🐝 Join Here', url='https://t.me/honeybeemovies'),
            InlineKeyboardButton('Updates 🎬', url='https://t.me/malluflix'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if Config.msg.get('pleh') is not None:
        await Config.msg['pleh'].delete()
    Config.msg['pleh'] = await message.reply_text(
        Config.HELP,
        reply_markup=reply_markup
        )
@Client.on_message(filters.command(['uk', f"uk@{Config.BOT_USERNAME}"]))
async def uk_(client, message):
        await message.reply("Podi Galli 😘❤️")

@Client.on_message(filters.command(['restart', 'update', f"restart@{Config.BOT_USERNAME}", f"update@{Config.BOT_USERNAME}"]) & admin_filter)
async def update_handler(client, message):
    await message.reply("Updating and restarting the bot.")
    await update()

@Client.on_message(filters.command(['logs', f"logs@{Config.BOT_USERNAME}"]) & admin_filter)
async def get_logs(client, message):
    logs=[]
    if os.path.exists("ffmpeg.txt"):
        logs.append(InputMediaDocument("ffmpeg.txt", caption="FFMPEG Logs"))
    if os.path.exists("ffmpeg.txt"):
        logs.append(InputMediaDocument("botlog.txt", caption="Bot Logs"))
    if logs:
        await message.reply_media_group(logs)
        logs.clear()
    else:
        await message.reply("No log files found.")
