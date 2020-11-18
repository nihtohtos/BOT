from telethon import TelegramClient, events
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = 2972564
api_hash = 'bd016c365603666a9ad778ee3ef06e65'
bot_token = '1387337520:AAFnzLm_vCzLKHteimP0ARtVnS09ZXCqKE4'
bot = TelegramClient('Jeanbot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern=r'\.мут'))
async def mute(event):
    replied = await event.get_reply_message()
    user = replied.sender
    muter = event.sender
    chat = await event.get_chat()
    permissions = await bot.get_permissions(chat, muter)
    if permissions.delete_messages == True:
        await bot.edit_permissions(chat, user, send_messages = False)
        await event.reply("Замучено!")
    else:
        await event.reply("У вас немає прав.")

@bot.on(events.NewMessage(pattern=r'\.розмут'))
async def unmute(event):
    replied2 = await event.get_reply_message()
    user2 = replied2.sender
    muter2 = event.sender
    chat2 = await event.get_chat()
    permissions2 = await bot.get_permissions(chat2, muter2)
    if permissions2.delete_messages == True:
        await bot.edit_permissions(chat2, user2, send_messages = True)
        await event.reply("Розмучено!")
    else:
        await event.reply("У вас немає прав.")

@bot.on(events.NewMessage(pattern=r'\.бан'))
async def ban(event):
    replied3 = await event.get_reply_message()
    user3 = replied3.sender
    baner = event.sender
    chat3 = await event.get_chat()
    permissions3 = await bot.get_permissions(chat3, baner)
    if permissions3.ban_users == True:
        await bot.edit_permissions(chat3, user3, view_messages = False)
        await event.reply("Забанено!")
    else:
        await event.reply("У вас немає прав.")

@bot.on(events.NewMessage(pattern=r'\.розбан'))
async def unbaner(event):
    replied4 = await event.get_reply_message()
    user4 = replied4.sender
    baner2 = event.sender
    chat4 = await event.get_chat()
    permissions4 = await bot.get_permissions(chat4, baner2)
    if permissions4.ban_users == True:
        await bot.edit_permissions(chat4, user4, view_messages = True)
        await event.reply("Розбанено!")
    else:
        await event.reply("У вас немає прав.")

@bot.on(events.NewMessage(pattern=r'\.кік'))
async def kicker(event):
    replied5 = await event.get_reply_message()
    user5 = replied5.sender
    kicker = event.sender
    chat5 = await event.get_chat()
    permissions5 = await bot.get_permissions(chat5, kicker)
    if permissions5.ban_users == True:
        await bot.edit_permissions(chat5, user5, view_messages = False)
        await bot.edit_permissions(chat5, user5, view_messages = True)
        await event.reply("Кікнуто!")
    else:
        await event.reply("У вас немає прав.")

bot.start()
bot.run_until_disconnected()
