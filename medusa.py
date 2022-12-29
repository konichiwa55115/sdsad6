from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME
from pyrogram import Client, filters, idle
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

Medusa = Client(
    session_name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root='plugins')
)


PMTEXT = (
   "أنا بوت أقوم بتحميل الدروس من يوتيوب . \n\n فقط اكتب اسم الدرس الذي تريد مسبوقاً بالأمر /get \n\n مثلاً \n\n /get شرح شمس الحديث 01 \n\n ممنوع استخدام البوت لتحميل الأغاني أو الشيلات أو الأناشيد الإسلامية أو أي شيء حرام  \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 \n\n ممنوع استخدام البوت لتحميل الأغاني أو الموسيقا أو الشيلات أو الأناشيد الإسلامية أو أي شيء حرام \n\n . يمكنك التبرع لاستمرار المشروع من هنا \n\n (http://paypal.me/kelectronic89)"
)
PMKEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                'Help ❓', callback_data='help_callback'),
            InlineKeyboardButton('About ❕', callback_data='about')
        ],
        [
            InlineKeyboardButton(
                'Add me to a group 🎊', url='http://t.me/audmergbot?startgroup=true')  # Replace the `MedusaMousikibot` with your bot username
        ]
    ]
)
HELPTEXT = (
    '**Help Menu:**\n\nIf u need to download a song,'
    ' u should follow the syntax shown as below.\n\n'
    '•`/song <name of the song>`\n\nIf u need to extract lyrics,'
    ' follow the syntax shown as bellow.\n\n•`/lyrics <query>`'
)
ABOUTTEXT = (
    "**Name** : MedusaMusic🎵\n**Username** : MedusaMousikibot\n**Description**"
    " : <a href='https://en.wikipedia.org/wiki/Medusa'>**Medusa**</a> is a Greek"
    " mythology.\n__Generally described as winged human females with living"
    " venomous snakes in place of hair. Those who gazed into her eyes would"
    " turn to stone.\nThe word '**Mousiki**' is the Greek word for"
    " '**Music**'.__\n**Version** : 2.3.1\n**Special Credits:**\n\t•Credit of"
    " lyrics: __genius.com__\n\nProject by Bibee"
)


@Medusa.on_message(
    filters.command(['start', 'help'], ['/', '!'])
    & (filters.private | filters.group)
    & ~ filters.edited
)
async def start_cmd(_, msg: Message):
    ''' Response for /start command (private or groupe) '''

    if msg.chat.type == 'private':
        
        await msg.reply(
            text=PMTEXT,
            reply_markup=PMKEYBOARD,
            disable_web_page_preview=True
        )
    else:
        await msg.reply(
            text='Hey! I am Online. PM me if you have any question on how to use me.',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text='Start me in PM :)',
                            # Replace the `MedusaMousikibot` with your bot username
                            url=f't.me/audmergbot?start=help'
                        )
                    ]
                ]
            )
        )


@Medusa.on_callback_query()
async def callback_handling(_, query: CallbackQuery):
    ''' Response for Callback queries '''

    q_data = query.data
    q_id = query.id

    if q_data == 'menu_1':
        await Medusa.answer_callback_query(q_id, 'Main Menu!')
        await query.message.edit(
            text=PMTEXT,
            reply_markup=PMKEYBOARD,
            disable_web_page_preview=True
        )

    elif q_data == 'help_callback':
        await Medusa.answer_callback_query(q_id, 'Help Menu!')
        await query.message.edit(text=HELPTEXT,
                                 parse_mode='md',
                                 reply_markup=InlineKeyboardMarkup(
                                     [
                                         [
                                             InlineKeyboardButton(
                                                 text="Back",
                                                 callback_data='menu_1',
                                             )
                                         ]
                                     ]
                                 ),
                                 )

    elif q_data == 'about':
        await Medusa.answer_callback_query(q_id, text='About Menu!')
        await query.message.edit(
            text=ABOUTTEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            'Back', callback_data='menu_1')
                    ]
                ]
            )
        )




Medusa.start()
print('Medusa is starting....')
idle()
print('Medusa is aborting...')
Medusa.stop()
