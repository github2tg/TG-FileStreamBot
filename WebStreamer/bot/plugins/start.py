# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'ℍ𝕚 {m.from_user.mention(style="md")}, 𝕊𝕖𝕟𝕕 𝕞𝕖 𝕒 𝕗𝕚𝕝𝕖 𝕥𝕠 𝕘𝕖𝕥 𝕒𝕟 𝕚𝕟𝕤𝕥𝕒𝕟𝕥 𝕤𝕥𝕣𝕖𝕒𝕞 𝕝𝕚𝕟𝕜.\n\nപിന്നെ ഒരുകാര്യം ബോട്ട് start കൊടുത്തിട്ട് reply വരുന്നില്ല എങ്കിൽ താഴെ പറയുന്നലിങ്കിൽ ഒന്ന് ക്ലിക്ക് ചെയ്ത് open ചെയ്ത് തിരിച്ച് വരുക അപ്പൊ ശെരിയാകും\n\n┈┈┈••✿ 👇👇🅻︎🅸︎🅽︎🅺︎👇👇 ✿••┈┈┈.',
                  reply_markup=InlineKeyboardMarkup(
                      [[
                            InlineKeyboardButton(
                                  f'🅻︎🅸︎🅽︎🅺︎',
                                  url='https://mhnd-file-streem.herokuapp.com/')
                            InlineKeyboardButton(
                                  f'𝕁𝕆𝕀ℕ 𝕋ℍ𝕀𝕊 ℂℍ𝔸ℕℕ𝔼𝕃',
                                  url='https://telegram.me/MHND_BOT_UPDATE_CHANNEL')
                        ]]
                  ))
