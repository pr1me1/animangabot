from telegram import Update, ParseMode, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from constants import states, constants
from constants.constants import ERROR_TEXT, ERROR_VALIDATE, AGE, CONTACT, ERROR_MIS, REGISTER_SUCCESS
from database import add_user
from keyboards import reply
from keyboards.reply import main_keys
from utils import validations, get_translation as _


def validate_full_name(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    if update.message and not update.message.text:
        update.message.reply_text(_.translate(ERROR_TEXT, lang))
        return states.FULL_NAME

    if not validations.validate_full_name(update.message.text):
        update.message.reply_text(
            _.translate(ERROR_VALIDATE, lang), parse_mode=ParseMode.MARKDOWN_V2,
        )
        return states.FULL_NAME

    full_name = update.message.text.title()
    context.user_data['full_name'] = full_name

    update.message.reply_text(_.translate(AGE, lang))
    return states.AGE


def validate_age(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    if update.message and not update.message.text:
        update.message.reply_text(_.translate(ERROR_TEXT, lang))

        return states.AGE

    if not update.message.text.isdigit():
        age = validations.string_to_num(update.message.text)
    else:
        age = int(update.message.text)

    if age not in range(12, 99):
        update.message.reply_text(_.translate(ERROR_VALIDATE, lang), parse_mode=ParseMode.MARKDOWN_V2, )
        return states.AGE

    context.user_data['age'] = age
    update.message.reply_text(_.translate(CONTACT, lang), reply_markup=reply.get_contact())
    return states.CONTACT


def validate_contact(update: Update, context: CallbackContext):
    lang = context.user_data.get('lang')
    if update.message and not update.message.contact:
        update.message.reply_text(_.translate(CONTACT, lang),
                                  reply_markup=reply.get_contact())
        return states.CONTACT

    if not update.message.contact.user_id == update.message.from_user.id:
        update.message.reply_text(_.translate(ERROR_MIS, lang),
                                  reply_markup=reply.get_contact())
        return states.CONTACT

    phone = update.message.contact.phone_number
    context.user_data['phone'] = phone
    message = "<b>Yangi foydalanuvchi:</b>\n\n"
    message += f"full_name: {str(context.user_data['full_name'])}"
    message += f"\nage: {str(context.user_data['age'])}"
    message += f"\nphone: {str(context.user_data['phone'])}"

    add_user(telegram_id=update.message.from_user.id, full_name=context.user_data['full_name'])

    update.message.reply_text(f"{context.user_data['full_name']} {_.translate(REGISTER_SUCCESS, lang)}",
                              reply_markup=main_keys())

    for admin in constants.ADMINS:
        context.bot.send_message(admin, message, parse_mode=ParseMode.HTML)

    return states.END
