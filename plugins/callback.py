# (c) ShuhaibNC

#pylint:disable=E0602
#pylint:disable=E0401
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import time
import config
import Script
from funcs import *

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
                        await query.message.edit_reply_markup(reply_markup)
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
                            [InlineKeyboardButton('🌚 Emoji to Image',url='https://t.me/NightAIBot?emoji')],
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
                        await query.answer('Fetching...')
                        fd = await query.message.reply('Fetching data....')
                        button = [
                            [InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ', callback_data='close')]
                        ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await fd.edit(f'<b>Total Confirmed 🦠</b>: <code>{covid()}</code>', reply_markup=reply_markup)
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