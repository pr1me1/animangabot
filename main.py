from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

from constants import states
from database import create_user_table
from handlers import commands, callback, registration
from handlers.anime import choose_button, get_anime_keys, start_search, search_action


def main() -> None:
    create_user_table()
    updater = Updater("7338253696:AAHksCn6_vL9Y7wuWIIId503nhvYvkXqSCw")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", commands.start))
    dispatcher.add_handler(CommandHandler("language", commands.set_language))
    dispatcher.add_handler(CommandHandler("help", commands.help))
    dispatcher.add_handler(CommandHandler("unregister", commands.unregister))

    dispatcher.add_handler(CallbackQueryHandler(callback.set_language))

    dispatcher.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("register", commands.register),
        ],
        states={
            states.FULL_NAME: [
                MessageHandler(Filters.all, registration.validate_full_name),
            ],
            states.AGE: [
                MessageHandler(Filters.all, registration.validate_age),
            ],
            states.CONTACT: [
                MessageHandler(Filters.all, registration.validate_contact)
            ],
        },
        fallbacks=[
            CommandHandler("help", commands.help)
        ]
    ))

    dispatcher.add_handler(ConversationHandler(
        entry_points=[
            MessageHandler(Filters.text("Anime"), get_anime_keys),
        ],
        states={
            states.WAITING_BUTTON: [
                MessageHandler(Filters.text, choose_button)
            ],
            states.SEARCH_ANIME: [
                MessageHandler(Filters.text, start_search)
            ],
            states.SEARCHED: [
                CallbackQueryHandler(search_action)
            ]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

# dispatcher.add_handler(MessageHandler(Filters.text(["Sevimli ⭐️", "Избранное ⭐️", "Favorite ⭐️"]), get_saved_anime))
# dispatcher.add_handler(
#     ConversationHandler(
#         entry_points=[
#             MessageHandler(Filters.text(["Qidirish 🔍", "Поиск 🔍", "Search 🔍"]), start_search),
#         ],
#         states={
#             states.SEARCH_ANIME: [
#                 MessageHandler(Filters.all, search_anime),
#             ],
#         },
#         fallbacks=[
#             CommandHandler("help", commands.help)
#         ]
#     )
# )

# dispatcher.add_handler(
#     ConversationHandler(
#         entry_points=[
#             MessageHandler(Filters.text("Anime"), get_anime_keys)
#         ],
#         states={
#             states.SEARCH: [
#                 MessageHandler(Filters.text(["Qidirish 🔍", "Поиск 🔍", "Search 🔍"]), search_anime)
#             ],
#             states.RECOMMENDATION: [
#                 MessageHandler(Filters.text(["Tavsiya 🔥", "Рекомендация 🔥", "Recommendation 🔥"]),
#                                get_recommended_anime)],
#             states.RANDOM: [
#                 MessageHandler(filters=Filters.text(["Tasodifiy 🎲", "Случайно 🎲", "Random 🎲"]),
#                                callback=get_random_anime)],
#             states.FAVOURITE: [
#                 MessageHandler(Filters.text(["Sevimli ⭐️", "Избранное ⭐️", "Favorite ⭐️"]), get_saved_anime)],
#
#         },
#         fallbacks=[CommandHandler("help", commands.help)]
#     )
# )

# dispatcher.add_handler(MessageHandler(Filters.text("Anime"), get_anime_keys))
# dispatcher.add_handler(
#     MessageHandler(Filters.text(["Tavsiya 🔥", "Рекомендация 🔥", "Recommendation 🔥"]), get_recommended_anime))
# dispatcher.add_handler(
#     MessageHandler(filters=Filters.text(["Tasodifiy 🎲", "Случайно 🎲", "Random 🎲"]), callback=get_random_anime))
