from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import Script
import requests
import config
import html
import json
import asyncio
from funcs import *
import uuid
import os


link_dict = {}

#ping
@Client.on_message(filters.command('ping') & filters.incoming)
async def ping(client, message):
                start_time = time.time()
                m = await message.reply('Pinging....', quote=True)
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000
                await m.edit(f'Pong!\n{elapsed_time:.3f}ms')
                
#start
@Client.on_message(filters.command('start'))
async def start(client, message):
    if len(message.command) > 1 and message.command[1].startswith("upload_"):
        key = message.command[1][7:]
        real_url = link_dict.get(key)
        try:
            response = requests.get(real_url, stream=True, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            filename = await sanitize_filename(await get_filename_from_cd(response) or f"file_{key}.srt")
            k = await message.reply(f"Uploading: <code>{filename}</code>", quote=True)
            with open(filename, "wb") as f:
                f.write(response.content)

            await client.send_document(
                chat_id=message.from_user.id,
                document=filename,
                caption=f"📁 Filename : <code>{filename}</code>",
                parse_mode=enums.ParseMode.HTML
            )
            time.sleep(2)
            await k.delete()
        except Exception as e:
            await k.edit(f"Failed to upload the file.\n {e}")
        finally:
            if os.path.exists(filename):
                os.remove(filename)  # clean up
    thunder = await message.reply('⚡')
    await asyncio.sleep(1)
    await thunder.delete()
    button = [
    [InlineKeyboardButton('Menu 🌌', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(button)
    await message.reply(Script.START_TEXT, reply_markup=reply_markup, quote=True)
                
#help
@Client.on_message(filters.command('help') & filters.incoming)
async def help(client, message):
                await message.reply(Script.HELP_TEXT)
                
@Client.on_message(filters.command('stats') & filters.incoming)
async def stats(client, message):
                await message.reply(Script.STATUS_TXT)
 
#id filter               
@Client.on_message(filters.command('id') & filters.incoming)
async def whois(client, message):
                message = message.reply_to_message or message
                first = message.from_user.first_name
                last = message.from_user.last_name
                id = message.from_user.id
                username = message.from_user.username
                dc = message.chat.dc_id
                chatid = message.chat.id
                button = [
                            [InlineKeyboardButton('❌ Close', callback_data='close')]
                        ]
                reply_markup = InlineKeyboardMarkup(button)
                await message.reply_text(Script.ID_TEXT.format(first, last, username, id, dc, chatid), reply_markup=reply_markup)

@Client.on_message(filters.command('echo') & filters.text)
async def echofunc(client, message):
    if message.reply_to_message:
        # Replied message, use its text
        cmd = message.reply_to_message.text or message.reply_to_message.caption or ""

    elif len(message.text.split(' ', 1)) > 1:
        # Command has argument like /echo something
        cmd = message.text.split(' ', 1)[1]

    else:
        # No reply and no extra text
        return await message.reply(
            "<b>Example:</b>\n<code>/echo Who are you?</code>",
            parse_mode=enums.ParseMode.HTML
        )

    if len(cmd) > 4096:
        return await message.reply("Message too long! Please keep it under 4096 characters.")

    await client.send_message(
        chat_id=message.chat.id,
        text=cmd,
        reply_to_message_id= message.reply_to_message.id if message.reply_to_message else message.id,
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command('blockanimation') & filters.incoming)
async def blockanimation(bot, message):
    msg = await bot.send_message(
        chat_id=message.chat.id,
        text="⬜",
        reply_to_message_id= message.reply_to_message.id if message.reply_to_message else message.id,
        disable_web_page_preview=True,
    )
    for x in range(18):
        await msg.edit(Script.block_chain[x%18])
        time.sleep(1)
    await msg.edit('🟥')

@Client.on_message(filters.command('bombs') & filters.incoming)
async def bombs(bot, update):
    msg = await bot.send_message(
        chat_id=update.chat.id,
        text="💣",
        reply_to_message_id= update.reply_to_message.id if update.reply_to_message else update.id,
        disable_web_page_preview=True,
    )
    for x in range(9):
        await msg.edit(Script.bomb_ettu[x%9])
        time.sleep(1)
    await msg.edit('RIP PLOX...')

@Client.on_message(filters.command('hack') & filters.text)
async def hack(bot, update):
    if len(update.command) < 2:
        return await update.reply('<b>Example:</b>\n<code>/hack @JamesW</code>', )
    cmd = update.text.split(' ', 1)[1]
    msg = await bot.send_message(
        chat_id=update.chat.id,
        text=f'Target {cmd} selected',
        reply_to_message_id= update.reply_to_message.id if update.reply_to_message else update.id,
        disable_web_page_preview=True,
    )
    for x in range(10):
        await msg.edit_text(Script.hack_you[x%5])
        time.sleep(1)
    await msg.edit(f'Successfully hacked {cmd}\'s all data and sent to Admin\'s Database.')


@Client.on_message(filters.command('love') & filters.incoming)
async def love(bot, update):
    msg = await bot.send_message(
        chat_id=update.chat.id,
        text='❣️',
        reply_to_message_id= update.reply_to_message.id if update.reply_to_message else update.id,
        disable_web_page_preview=True,
    )
    for x in range(10):
        await msg.edit(Script.love_siren[x%5])
        time.sleep(1)
    await msg.edit('True Love💞')

@Client.on_message(filters.command('msone') & filters.incoming)
async def msone(bot, message):
    if len(message.command) < 2:
        return await message.reply('<b>Example:</b>\n<code>/msone Titanic</code>')
    
    res = await message.reply('Searching...', quote=True)
    cmd = message.text.split(' ', 1)[1]
    buttons = []
    download_links = []
    headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://google.com"
}
    titles = await msonescrap(cmd, 'title')
    links = await msonescrap(cmd, 'link')
    # titles, links = remove_duplicates(titles, links)
    for link in links:
        resp = requests.get(link, headers=headers, timeout=10)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        dl_btn = soup.select_one("a#download-button")
        download_links.append(dl_btn.get("data-downloadurl"))
        
    
    
    if titles == 'Nothing' or links == 'Nothing':
        return await res.edit('No results found.')
    else:
        i = 0
        while i < len(titles):
            key = str(uuid.uuid4())[:8]
            link_dict[key] = download_links[i]
            buttons.append([InlineKeyboardButton(titles[i], url=f"https://t.me/NightAiBot?start=upload_{key}")])
            i += 1
        buttons.append([InlineKeyboardButton('❌ CLOSE', callback_data='close_data')])
        markup = InlineKeyboardMarkup(buttons)
        await res.edit(f'Here is your result for your query {cmd}', reply_markup=markup)

@Client.on_message(filters.command('github') & filters.text)        
async def github(bot, message):
    if len(message.command) < 2:
        return await message.reply('<b>Example:</b>\n<code>/github torvalds</code>')
    
    res = await message.reply('Searching...', quote=True)
    username = message.text.split(' ', 1)[1]
    headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://google.com"
}
    usr = requests.get(f'https://api.github.com/users/{username}', headers=headers).json()
    if usr.get('login'):
        reply_text = f"""<b>Name:</b> <code>{usr.get('name') or 'N/A'}</code>
<b>Username:</b> <code>{usr['login']}</code>
<b>Account ID:</b> <code>{usr['id']}</code>
<b>Account type:</b> <code>{usr['type']}</code>
<b>Site Admin:</b> <code>{usr.get('site_admin', False)}</code>
<b>User View Type:</b> <code>{usr.get('user_view_type', 'N/A')}</code>
<b>Location:</b> <code>{usr.get('location') or 'N/A'}</code>
<b>Bio:</b> <code>{usr.get('bio') or 'N/A'}</code>
<b>Followers:</b> <code>{usr.get('followers')}</code>
<b>Following:</b> <code>{usr.get('following')}</code>
<b>Hireable:</b> <code>{usr.get('hireable') or 'N/A'}</code>
<b>Public Repos:</b> <code>{usr.get('public_repos')}</code>
<b>Public Gists:</b> <code>{usr.get('public_gists')}</code>
<b>Email:</b> <code>{usr.get('email') or 'N/A'}</code>
<b>Company:</b> <code>{usr.get('company') or 'N/A'}</code>
<b>Twitter:</b> <code>{usr.get('twitter_username') or 'N/A'}</code>
<b>Website:</b> <code>{usr.get('blog') or 'N/A'}</code>
<b>Avatar URL:</b> <a href="{usr.get('avatar_url')}">Link</a>
<b>Profile URL:</b> <a href="{usr['html_url']}">GitHub</a>
<b>Last Updated:</b> <code>{usr.get('updated_at')}</code>
<b>Account Created At:</b> <code>{usr.get('created_at')}</code>
"""
    else:
        reply_text = "User not found. Make sure you entered valid username!"
    await message.reply_photo(usr.get('avatar_url'), caption=reply_text, parse_mode=enums.ParseMode.HTML)
    await res.delete()
@Client.on_message(filters.command('lyrics') & filters.text)   
async def lyrics(bot, update):
    if len(update.command) < 2:
        return await update.reply('<b>Example:</b>\n<code>/lyrics Middle of the night</code>')
    query = update.text.split(' ', 1)[1]
    k = await update.reply(f'Searching for {query}...')
    
    headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://google.com"
}

    res = requests.get(f'https://lrclib.net//api/search?q={html.escape(query)}', headers=headers)
    try:
        lyric = json.loads(res.text)[0]['plainLyrics']
    except (json.JSONDecodeError, IndexError):
        lyric = None
    if lyric:
        await k.edit(f'Lyrics for <b>{query}</b>:\n\n<code>{lyric}</code>', parse_mode=enums.ParseMode.HTML)
    else:
        await k.edit('No lyrics found for this song.')
    