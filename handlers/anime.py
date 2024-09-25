import asyncio

from telegram import Update
from telegram.ext import CallbackContext

from constants import states
from constants.constants import CHOOSE, ERROR_TEXT, SEARCH, SEARCH_ANIME, RANDOM, FAVOURITE, CURRENT_ANIME_PAGE
from constants.languages import TRANSLATIONS
from jikan.anime import get_random_anime_by_jikan, search_anime_by_jikan
from keyboards.inline import get_anime_inlines
from keyboards.reply import anime_keys, back, main_keys
from utils.anime_formater import anime_format, anime_list_format
from utils.get_translation import translate


def get_anime_keys(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    update.message.reply_text(translate(CHOOSE, lang), reply_markup=anime_keys(lang))
    return states.WAITING_BUTTON


def choose_button(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    if not update.message.text:
        update.message.reply_text(translate(ERROR_TEXT, lang))

    if list(TRANSLATIONS.get(SEARCH).values()).__contains__(update.message.text):
        update.message.reply_text(translate(SEARCH_ANIME, lang), reply_markup=back())
        return states.SEARCH_ANIME

    if list(TRANSLATIONS.get(RANDOM).values()).__contains__(update.message.text):
        result = asyncio.run(get_random_anime_by_jikan())
        update.message.reply_photo(photo=result.get('data').get('images').get('jpg').get('image_url'),
                                   caption=anime_format(result.get('data')), parse_mode="html")
        update.message.reply_text("Synopsis: " + str(result.get('data').get('synopsis')) + '\n', reply_markup=back())
        return states.RANDOM

    if list(TRANSLATIONS.get(FAVOURITE).values()).__contains__(update.message.text):
        # get saveds
        pass

    if list(TRANSLATIONS.get(SEARCH).values()).__contains__(update.message.text):
        pass

    if update.message.text == "⬅️":
        lang = context.user_data.get('lang')
        update.message.reply_text(translate(CHOOSE, lang), reply_markup=main_keys())
        return states.END


def start_search(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    context.user_data[CURRENT_ANIME_PAGE] = current = 1

    if update.message and not update.message.text:
        update.message.reply_text(translate(ERROR_TEXT, lang))

    if update.message == "⬅️":
        update.message.reply_text(translate(CHOOSE, lang), reply_markup=anime_keys(lang))
        return states.WAITING_BUTTON

    result = asyncio.run(
        search_anime_by_jikan(anime_name=update.message.text, page=context.user_data[CURRENT_ANIME_PAGE]))
    update.message.reply_text(anime_list_format(result.get('data')),
                              reply_markup=get_anime_inlines(result.get('data')))

    return states.SEARCHED


def search_action(update: Update, context: CallbackContext):
    print("search_anime: ive worked")

    context.user_data[CURRENT_ANIME_PAGE] = context.user_data[CURRENT_ANIME_PAGE] + 1

    lang = context.user_data.get('lang')

#
#
# def get_random_anime(update: Update, context: CallbackContext):
#     result = asyncio.run(get_random_anime_by_jikan())
#     update.message.reply_photo(photo=result.get('data').get('images').get('jpg').get('image_url'),
#                                caption=anime_format(result.get('data')), parse_mode="html")
#     update.message.reply_text("Synopsis: " + str(result.get('data').get('synopsis')) + '\n')
#     pass
#
#
# def get_recommended_anime(update: Update, context: CallbackContext):
#     pass
#
#
# def get_saved_anime(update: Update, context: CallbackContext):
#     pass
#
#
# def back_main(update: Update, context: CallbackContext):
#     lang = context.user_data.get('lang')
#     update.message.reply_text(translate(CHOOSE, lang), reply_markup=main_keys())
