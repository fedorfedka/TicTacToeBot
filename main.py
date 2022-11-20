from telegram import *
from telegram.ext import *
from requests import *
import read_conf


updater = Updater(token=read_conf.TOKEN)
dispatcher = updater.dispatcher

is_game_on :bool = False
is_my_turn :bool = True

def start_command(update :Update, context :CallbackContext):
    buttons = [[KeyboardButton(read_conf.PB), KeyboardButton(read_conf.PH)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to TicTacToe bot by fedorfedka!",
        reply_markup=ReplyKeyboardMarkup(buttons)
        )


def message_handler(update :Update, context :CallbackContext):
    global is_game_on
    global is_my_turn
    if not is_game_on:
        if read_conf.PB in update.message.text:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='wip',
            )
            is_game_on = True


        if read_conf.PH in update.message.text:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="wip",
            )
    
    if is_game_on:
        buttons = [[KeyboardButton('Go on'), KeyboardButton('Stop')]]

        if is_my_turn:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Whach u wan",
                reply_markup=ReplyKeyboardMarkup(buttons)
                )
            is_my_turn = False
        if 'Go on' in update.message.text:
            pass
        elif 'Stop' in update.message.text:
            is_game_on = False
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=str(is_game_on)
        )
        

dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()