#pylint:disable=E0602
#pylint:disable=E0401
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import time
import config
import Script
from funcs import *
import speedtest
def convert(speed):
    return round(int(speed)/1048576, 2)
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
                        await query.message.edit_text(text=Script.START_TEXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
                    elif query.data == 'speedtest_image':
                        msg = await query.message.edit('Runing a speedtest....') 
                        speed = speedtest.Speedtest()
                        speed.get_best_server()
                        speed.download()
                        speed.upload()
                        replymsg = 'Speedtest Results:'
                        speedtest_image = speed.results.share()
                        await query.message.reply_photo(photo=speedtest_image, caption=replymsg)
                        await msg.delete()

                    elif query.data == 'speedtest_text':
                        msg = await query.message.edit('Runing a speedtest....') 
                        speed = speedtest.Speedtest()
                        speed.get_best_server()
                        speed.download()
                        speed.upload()
                        replymsg = 'Speedtest Results:'
                        result = speed.results.dict()
                        replymsg += f"\nDownload: `{convert(result['download'])}Mb/s`\nUpload: `{convert(result['upload'])}Mb/s`\nPing: `{result['ping']}`"
                        await query.message.edit(replymsg, parse_mode=enums.ParseMode.MARKDOWN)