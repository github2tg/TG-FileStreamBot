# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link\n\nപിന്നെ ഒരുകാര്യം ബോട്ട് start കൊടുത്തിട്ട് "
                  "reply വരുന്നില്ല എങ്കിൽ താഴെ പറയുന്നലിങ്കിൽ ഒന്ന് ക്ലിക്ക് ചെയ്ത് open ചെയ്ത് തിരിച്ച് വരുക അപ്പൊ ശെരിയാകും\n\nlink👉https://mhnd-file-streem.herokuapp.com/.',
                  reply_markup=InlineKeyboardMarkup(
                      [[
                            InlineKeyboardButton(
                                  f'JOIN THIS CHANNEL',
                                  url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL')
                        ]]
                  ))
