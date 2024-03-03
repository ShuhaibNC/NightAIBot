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
                                [InlineKeyboardButton('🤖AI',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton(' 🔑 PassGen', callback_data='pass_gen')],
                                [InlineKeyboardButton('💬Msone',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('⚙️ Run Python Code',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('😀 Emoji',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton(' 😀😁Emix',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('🌚 Emoji to Image',url='https://t.me/NightAiBot?emoji')],
                                 [InlineKeyboardButton('🟣 Thanos Quote', url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('🦠 Covid data', url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('🆔 ID',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('📍 Ping', url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('🔉 Echo',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('📜 Stats',url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('🆘 Help', url='https://t.me/NightAiBot?emoji')],
                                [InlineKeyboardButton('🔙 Back', callback_data='help')] ]
                        reply_markup = InlineKeyboardMarkup(button)
                        await query.message.edit_text(Script.FEATURES)
                        
                        
                    elif query.data == 'id_refresh':
                        await query.message.edit_text('Okay Refreshed. Now what?')