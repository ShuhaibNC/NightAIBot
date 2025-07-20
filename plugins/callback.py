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
                            [InlineKeyboardButton('🏡 Home', callback_data='start'),
                            InlineKeyboardButton('🔐 Close', callback_data='close_data')]
                        ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await query.message.edit(reply_markup=reply_markup, text=Script.HELP_TEXT)
                    #close
                    elif query.data == 'close_data':
                        await query.message.delete()
                    #start
                    elif query.data == 'start':
                        button = [
                [InlineKeyboardButton('Menu 🌌', callback_data='help')]
                ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await query.message.edit_text(text=Script.START_TEXT, reply_markup=reply_markup)