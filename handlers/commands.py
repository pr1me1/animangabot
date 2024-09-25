import asyncio

from telegram.ext import CallbackContext
from telegram import Update, ParseMode, ReplyKeyboardRemove
from constants import constants, states
from constants.constants import *
from database import check_user, unregister_user
from keyboards.reply import main_keys
from utils.get_translation import translate as _
from keyboards.inline import get_language


def start(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    x = asyncio.run(check_user(telegram_id=update.message.from_user.id))
    if x:
        update.message.reply_text(_(GREETING, lang), reply_markup=main_keys())
    else:
        update.message.reply_text(_(GREETING, lang) + "\n\n" + _(ERROR_NOT_REGISTERED, lang))


def set_language(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    mes = update.message.reply_text("...", reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=mes.message_id)
    update.message.reply_text(_(SET_LANGUAGE, lang), reply_markup=get_language())


def help(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    update.message.reply_text(_(HELP, lang), parse_mode=ParseMode.MARKDOWN_V2, reply_markup=ReplyKeyboardRemove())


def register(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')

    x = asyncio.run(check_user(telegram_id=update.message.from_user.id))
    if x:
        update.message.reply_text(_(ERROR_REGISTERED, lang), reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(_(REGISTER, lang), reply_markup=ReplyKeyboardRemove())
        return states.FULL_NAME


def unregister(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    x = asyncio.run(check_user(telegram_id=update.message.from_user.id))
    if x:
        asyncio.run(unregister_user(telegram_id=update.message.from_user.id))
        update.message.reply_text(_(UNREGISTER, lang), reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(_(ERROR_NOT_REGISTERED, lang), reply_markup=ReplyKeyboardRemove())
