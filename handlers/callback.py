from telegram import Update
from telegram.ext import CallbackContext

from keyboards.reply import main_keys
from utils.get_translation import translate as _
from constants.constants import *


def set_language(update: Update, context: CallbackContext):
    context.user_data['lang'] = update.callback_query.data
    update.callback_query.answer()
    update.callback_query.message.reply_text(_(LANGUAGE_CHANGED, update.callback_query.data), reply_markup=main_keys())
    update.callback_query.message.delete()
