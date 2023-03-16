# (c) ShuhaibNC

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
                [InlineKeyboardButton('ᴍᴇɴᴜ 🌌', callback_data='help')]
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
                cmd = message.text.split(' ', 1)[1]
                try:
                    out = run_code(cmd)
                    await message.reply(f'Output:\n<code>{out}</code>', quote=True)
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
                await message.reply(Script.STATS_TXT.format(users, cpu_usage, ram_usage, ram, storage_usage, total_storage, uptime), message.chat.id)

@Client.on_message(filters.command('emoji') & filters.incoming)
async def cmdemoji(client, message):
    if len(message.command) < 2:
        return await message.reply('Example:\n<code>/emoji 🌚</code>')
    await client.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
    text = message.command[1]
    #text : Message = await client.listen(message.chat.id)
    await message.reply_photo(photo=eemoji(text))
    
@Client.on_message(filters.command('emix') & filters.incoming)
async def myemix(client, message):
    if len(message.command) < 2:
        return await message.reply('Example:\n<code>/emix 😁😄</code>')
    await client.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
    text = message.command[1]
    await message.reply_photo(photo=emix(text))
    
@Client.on_message(filters.command('cat') & filters.incoming)
async def cat(client, message):
    await client.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
    await message.reply_photo(photo=catimage())
    
@Client.on_message(filters.command('msone') & filters.incoming)
async def msone(client, message):
    if len(message.command) < 2:
        return await message.reply('<b>Example:</b>\n<code>/msone Thor</code>')
    res = await message.reply('Searching...', quote=True)
    cmd = message.text.split(' ', 1)[1]
    buttons = []
    names = msonescrap(cmd, 'title')
    links = msonescrap(cmd, 'link')
    if names == 'Nothing' or links == 'Nothing':
        return await res.edit('No results found.')
    i = 0
    bu_list = []
    while i < len(names):
        if names[i] in bu_list:
            await message.reply('Removing...')
            i += 1
            pass
        else:
            buttons.append([InlineKeyboardButton(names[i], url= links[i])])
            bu_list.append(names[i])
            i += 1
            await message.reply(bu_list)
    buttons.append([InlineKeyboardButton('❌ CLOSE', callback_data='close')])
    markup = InlineKeyboardMarkup(buttons)
    await res.edit('Here is your result.', reply_markup=markup)
    
@Client.on_message(filters.command('thanos') & filters.incoming)
async def thanos(client, message):
    await message.reply(get_thanosquote())