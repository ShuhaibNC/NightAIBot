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
                [InlineKeyboardButton('ʙᴀᴄᴋ ⬅️', callback_data='help')]
                ]
                        reply_markup = InlineKeyboardMarkup(button)
                        
                        await query.message.edit_text(Script.FEATURES)
                        
                        
                    elif query.data == 'id_refresh':
                        await query.message.edit_text('Okay Refreshed. Now what?')