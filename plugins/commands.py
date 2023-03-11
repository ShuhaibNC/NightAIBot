#pylint:disable=E0602
#pylint:disable=E0401
from pyrogram import *
from pyrogram.types import *
import time
import Script
import config
from what import *
import asyncio
from funcs import *
import psutil
import subprocess

#ping
@Client.on_message(filters.command('ping') & filters.incoming)
async def ping(client, message):
                start_time = time.time()
                m = await message.reply('Pinging....')
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000
                await m.edit(f'Pong!\n{elapsed_time:.3f}ms')
                
#start
@Client.on_message(filters.command('start') & filters.incoming)
async def start(client, message):
                #thunder =await message.reply('⚡')
                #await asyncio.sleep(2)
                #await thunder.delete()
                button = [
                [InlineKeyboardButton('ʜᴇʟᴩ 🌌', callback_data='help')]
                ]
                reply_markup = InlineKeyboardMarkup(button)
                await message.reply(Script.START_TEXT, reply_markup=reply_markup, quote=True)
                
#help
@Client.on_message(filters.command('help') & filters.incoming)
async def help(client, message):
                await message.reply(Script.HELP_TEXT.format(message.from_user.mention), message.chat.first_name)
 
#id filter               
@Client.on_message(filters.command('id') & filters.incoming)
async def whois(client, message):
                first = message.from_user.first_name
                last = message.from_user.last_name
                id = message.from_user.id
                username = message.from_user.username
                dc = message.chat.dc_id
                chatid = message.chat.id
                button = [
                            [InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ', callback_data='close'), InlineKeyboardButton(' 🔄 Refresh', callback_data='id_refresh')]
                        ]
                reply_markup = InlineKeyboardMarkup(button)
                await message.reply_text(Script.ID_TEXT.format(first, last, username, id, dc, chatid), reply_markup=reply_markup)
                
                

@Client.on_message(filters.command('ai'))
async def aitext(client, message):
                if len(message.command) < 2:
                    return await message.reply("There are endless possibilities 🌌\n                         -MidjourneyAI")
                cmd = ''
                for i in message.command:
                    if i == message.command[0]:
                        continue
                    cmd = cmd + i + ' '
                headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.OPENAI_API}",
    }

                json_data = {
        "prompt": cmd,
        "model": "text-davinci-003",
        "temperature": 0.5,
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "top_p": 0.3,
        "frequency_penalty": 0.5, }
                
                response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
                await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
                await asyncio.sleep(5)
                try:
                    await client.send_message(message.chat.id, response["choices"][0]["text"], reply_to_message_id=message.id)
                except KeyError:
                    await client.send_message(message.chat.id, response['error']['message'], reply_to_message_id=message.chat.id)
                    
                    
@Client.on_message(filters.command('echo') & filters.text)
async def echofunc(client, message):
                if len(message.command) < 2:
                    return await message.reply('<b>Example:</b>\n<code>/echo Who are you?</code>', )
                r_txt = ''
                for i in message.command:
                    if i == message.command[0]:
                        continue
                    r_txt = r_txt + i +  ' '
                await message.reply_text(r_txt)
                

@Client.on_message(filters.command('run') & filters.incoming)
async def run(client, message):
                if len(message.command) < 2:
                    return await message.reply('<b>Example:</b>\n<code>/run print("Hello")</code>', )
                cmd = ''
                for i in message.command:
                    if i == message.command[0]:
                        continue
                    cmd = cmd + i + ' '
                try:
                    out = run_code(cmd)
                    await client.send_message(message.chat.id, f'Output:\n<code>{out}</code>', reply_to_message_id=message.chat.id)
                except Exception as e:
                    await message.reply(f'An error occured.\n\n{e}')
                    
@Client.on_message(filters.command('stats') & filters.incoming)
async def stats(client, message):
                cpu_usage = psutil.cpu_percent()
                users = '102'
                storage = psutil.disk_usage('/')
                storage_usage = storage.used / 1024
                total_storage = storage.total / 1024
                ram = psutil.virtual_memory()
                ram_usage = ram.used / (1024 ** 3)
                total_ram = ram.total / (1024 ** 3)
                uptime = subprocess.check_output(['uptime', '-p']).decode().strip('up').strip()
                await message.reply(Script.STATS_TXT.format(users, cpu_usage, f'{ram_usage:.2f}', f'{ram:.2f}', f'{storage_usage:.2f}', f'{total_storage:.2f}', uptime), message.chat.id)