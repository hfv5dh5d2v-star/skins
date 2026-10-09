from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

reply_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="JavaScript")
        ],
        [
            KeyboardButton(text="Java")
        ]
    ],
    resize_keyboard=True
)


inline_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Python', url = 'https://docs.python.org/3/')
        ],
        [
            InlineKeyboardButton(text = 'Java', url = 'https://docs.oracle.com/en/java/')
        ],
        [
            InlineKeyboardButton(text = 'JavaScript', url = 'https://developer.mozilla.org/en-US/docs/Web/JavaScript')
        ]
    ]
)

questions_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Начать тест', callback_data = 'start_test')
        ]
    ]
)