from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, enums
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent
)
import requests, bs4, uuid, asyncio
from plugins.commands import link_dict
from funcs import msonescrap 


@Client.on_inline_query()
async def inline_handler(bot, query: InlineQuery):
    q = query.query.strip()
    me = await bot.get_me()
    if not q:
        return await query.answer([
            InlineQueryResultArticle(
                title="Type something to search in MSONE Subtitles...",
                input_message_content=InputTextMessageContent(f"Try `@{me.username} Inception`"),
                description="MSONE Inline Search",
                thumbnail_url="https://malayalamsubtitles.org/wp-content/uploads/2025/03/msone-nav-id-icon.png",
            )
        ], cache_time=1)

    try:
        return await asyncio.wait_for(process_msone_inline(bot, query, q), timeout=4.8)
    except asyncio.TimeoutError:
        print("⚠️ Inline query timed out.")
    except Exception as e:
        print(f"⚠️ Inline error: {e}")


async def process_msone_inline(bot, query: InlineQuery, q: str):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://google.com"
    }

    titles = await msonescrap(q, 'title')
    links = await msonescrap(q, 'link')
    thumbs = await msonescrap(q, 'thumb')
    me = await bot.get_me()
    if titles == 'Nothing' or links == 'Nothing':
        return await query.answer([
            InlineQueryResultArticle(
                title="😔 No Results Found",
                input_message_content=InputTextMessageContent("Nothing found for your query.")
            )
        ], cache_time=1)

    results = []
    for title, link, thumb in zip(titles, links, thumbs):
        if link:
            key = str(uuid.uuid4())[:8]
            link_dict[key] = link
            results.append(
                InlineQueryResultArticle(
                    title=title,
                    thumbnail_url=thumb if thumb else "https://malayalamsubtitles.org/wp-content/uploads/2025/03/msone-nav-id-icon.png",
                    description=link,
                    input_message_content=InputTextMessageContent(
                        f"<b>🎬 Title : </b><code>{title}</code>\n\n<b>🔗 MSONE Link: </b>{link}\n\n<b>⬇️ Click Below Button to Upload File to Telegram...</b>",
                        parse_mode=enums.ParseMode.HTML
                    ),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔍 Search Again", switch_inline_query=q)],
                        [InlineKeyboardButton("🌐 Goto Download Page", url=link)],
                        [InlineKeyboardButton("⬇️ Download Now", url=f"https://t.me/{me.username}?start=upload_{key}")]
                                                       ])
                )
            )

    if not results:
        results.append(
            InlineQueryResultArticle(
                title="😐 No Downloadable Links",
                input_message_content=InputTextMessageContent("Found items, but no downloadable links.")
            )
        )

    return await query.answer(results, cache_time=2)
