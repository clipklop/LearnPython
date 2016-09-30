# Telegram chat bot
# with predefined answers

# TO-DO:
# handle users request which are absent in answers dict


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

answers = {
    'privet': 'Privetik, cowboy!',
    'kak dela': 'Poka ne rodila! A ti uje?',
    'poka': 'pokeda'
}

def get_answers(question, answers):
    return answers.get(question)

# def ask_user(answers):
#     user_input = update.message.text
#     answers = get_answers(user_input, answers)
#     return answers

#     # if update.message.text == 'poka':

def start(bot, update):
    print("Вызван /start!!11")
    bot.sendMessage(update.message.chat_id, text="Привет, чел. Как сам?")

def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    bot.sendMessage(update.message.chat_id, text=get_answers(update.message.text, answers))

def run_bot():
    updater = Updater("245205320:AAE8PoCVxD0W1-EDZ0myqEK5PriA4pihrcs")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run_bot()