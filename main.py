from telegram import *
from telegram.ext import *
from requests import *
import read_conf
import database_man


updater = Updater(token=read_conf.TOKEN)
dispatcher = updater.dispatcher

database_man.create_table(database_name=read_conf.DATABASE)

def start_command(update :Update, context :CallbackContext):
    buttons = [[KeyboardButton(read_conf.PB), KeyboardButton(read_conf.PH)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to TicTacToe bot by fedorfedka!",
        reply_markup=ReplyKeyboardMarkup(buttons)
        )

#main handler

def message_handler(update :Update, context :CallbackContext):
    if is_requester_in_game(update):
        context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='You are already in game!',
        )

    else:
        play_with_bot_handler(update, context)
        play_with_human_handler(update, context)
    

#handler funcs

def play_with_bot_handler(update :Update, context :CallbackContext):
    if read_conf.PB in update.message.text:
        context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='wip',
        )

def play_with_human_handler(update :Update, context :CallbackContext):
    if read_conf.PH in update.message.text:
        context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='wip',
        )
        is_requester_in_game(update)

#chekers
        
def is_requester_in_game(update :Update) -> bool:
    if database_man.find_by_requester(update.effective_user.name, read_conf.DATABASE) == []:
        return False

    return True


def is_accepter_in_game():
    pass


dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()