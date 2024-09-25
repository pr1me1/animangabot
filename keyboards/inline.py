from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from constants.constants import UZ, RU, EN


def get_language():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("O'zbek tili", callback_data=UZ)],
            [InlineKeyboardButton("Русский", callback_data=RU)],
            [InlineKeyboardButton("English", callback_data=EN)],
        ]
    )


def get_anime_inlines(anime: [{}]):
    keys = []

    for single_anime in anime:
        keys.append([InlineKeyboardButton(text=single_anime['title'], callback_data=single_anime['mal_id'])], )

    keys.append([InlineKeyboardButton(text="⬅️", callback_data="previous"),
                 InlineKeyboardButton(text="➡️", callback_data="next"), ])

    return InlineKeyboardMarkup(keys)
