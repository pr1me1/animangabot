from telegram import ReplyKeyboardMarkup, KeyboardButton

from constants.constants import SEARCH, RANDOM, RECOMMENDATION, FAVOURITE
from utils.get_translation import translate


def get_contact():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Telefon raqamni ulashish  📞", request_contact=True)]
        ],
        resize_keyboard=True,
    )


def main_keys():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Anime", ), KeyboardButton(text="Character")],
            [KeyboardButton(text="⭐️"), KeyboardButton(text="⚙️")]
        ],
        resize_keyboard=True,
    )


def anime_keys(lang: str):
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text=translate(SEARCH, lang), ), KeyboardButton(text=translate(RECOMMENDATION, lang), )],
            [KeyboardButton(text=translate(RANDOM, lang), ), KeyboardButton(text=translate(FAVOURITE, lang), )],
            [KeyboardButton(text="⬅️")]
        ],
        resize_keyboard=True,
    )


def back():
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text="⬅️"), ]],
        resize_keyboard=True,
    )
