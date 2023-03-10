#pylint:disable=E0401
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import time
import config
import requests
import random
import string
import Script
import re

def gen_pass():
        adjresp = requests.get("https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt")
        adj = random.choice(adjresp.text.split('\n'))
        nounresp = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
        noun = random.choice(nounresp.text.split("\n"))
        num = str(random.randrange(100))
        punct = random.choice(string.punctuation)
        passw = adj + noun + num + punct
        return passw
        
def covid():
    url = 'https://api.covid19api.com/world/total'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        total_cases = data['TotalConfirmed']
        return total_cases
    else:
        return 'Error retrieving data'



#callback handle
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery ):
                    #help callback vannal
                    if query.data == 'help':
                        
                        button = [
                            [InlineKeyboardButton('🐲 ꜰᴇᴀᴛᴜʀᴇꜱ', callback_data='mods')],
                            [InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='start'),
                            InlineKeyboardButton('🔐 ᴄʟᴏꜱᴇ', callback_data='close')]
                        ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await query.message.edit_text(text=Script.HELP_TEXT.format(query.from_user.mention), reply_markup=reply_markup)
                    #close
                    elif query.data == 'close':
                        await query.message.delete()
                    #start
                    elif query.data == 'start':
                        button = [
                [InlineKeyboardButton('ᴍᴇɴᴜ 🌌', callback_data='help')]
                ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await query.message.edit_text(text=Script.START_TEXT, reply_markup=reply_markup)
                    #mods
                    elif query.data == 'mods':
                        button = [
                            [InlineKeyboardButton(' 🔑 PassGen', callback_data='pass_gen')],
                            [InlineKeyboardButton('🦠 Covid', callback_data='covid')],
                            [InlineKeyboardButton('📍 Ping', callback_data='ping')],
                            [InlineKeyboardButton('🖥️ AI',callback_data='ai')],
                            [InlineKeyboardButton('🔙 Back',
                            callback_data='help')]
                        ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await query.message.edit_reply_markup(reply_markup)
                    #passgen
                    elif query.data == 'pass_gen':
                        button = [
                            [InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ', callback_data='close'), InlineKeyboardButton(' 🔄 Refresh', callback_data='pass_gen')]
                        ]
                        reply_markup = InlineKeyboardMarkup(button)
                        pw = await query.message.reply('Generating password....')
                        await pw.edit(f'🗨️ Your Password is : {gen_pass()}', reply_markup=reply_markup)
                        await query.answer('Revoking...')
                        await asyncio.sleep(3)
                        await pw.delete()
                    #covid
                    elif query.data == 'covid':
                        fd = await query.message.reply('Fetching data....')
                        await query.answer('Fetching')
                        button = [
                            [InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ', callback_data='close')]
                        ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await fd.edit(f'Total Confirmed 🦠: {covid()}', reply_markup=reply_markup)
                    #ping
                    elif query.data == 'ping':
                        button = [
                            [InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ', callback_data='close')]
                        ]
                        reply_markup = InlineKeyboardMarkup(button)
                        start_time = time.time()
                        pn = await query.message.reply('Pinging....')
                        end_time = time.time()
                        elapsed_time = (end_time - start_time) * 1000
                        await pn.edit(f'Pong!\n{elapsed_time:.3f}ms', reply_markup=reply_markup)
                    elif query.data == 'id_refresh':
                        await query.message.edit_text('Okay Refreshed. Now what?')
                    elif query.data == 'ai':
                        await query.answer('Coming soon... 🌚', show_alert=True)