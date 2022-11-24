from telegram import *
from telegram.ext import *
from requests import *
import read_conf

import game_logic


updater = Updater(token=read_conf.TOKEN)
dispatcher = updater.dispatcher

#create and rewrite sessions list
game_logic.create_session_list()

def start_command(update :Update, context :CallbackContext):
    buttons = [[KeyboardButton(read_conf.PB), KeyboardButton(read_conf.PH)]]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to TicTacToe bot by fedorfedka!",
        reply_markup=ReplyKeyboardMarkup(buttons)
        )


def stop_command(update :Update, context :CallbackContext):
    if game_logic.is_requester_in_game(update.effective_user.id):
        #
        game_logic.delete_session_by_requester(update.effective_user.id)
        #
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You are left the game",
            )
    else:    
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You are not in the game!",
            )   


#main handler

def message_handler(update :Update, context :CallbackContext):

    #cheks if user in game
    if game_logic.is_requester_in_game(update.effective_user.id):
        turns_handler(update, context)

    else:
        play_with_bot_handler(update, context)
        play_with_human_handler(update, context)
    

def turns_handler(update :Update, context :CallbackContext):
    global user_input
    global user_input_chat
    global procces_message

    if '1' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 0, 0)
        
        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '2' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 0, 1)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '3' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 0, 2)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '4' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 1, 0)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '5' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 1, 1)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '6' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 1, 2)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '7' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 2, 0)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '8' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)
        
        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 2, 1)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    if '9' in update.message.text:
        try:
            context.bot.delete_message(user_input_chat, user_input)
        except Exception as e:
            print(e)

        game_logic.edit_session_grid(game_logic.get_session_id_by_requester_id(update.effective_user.id), 2, 2)

        user_input = update.message.message_id
        user_input_chat = update.effective_chat.id

    game_logic.update_session_grid_png(game_logic.get_session_id_by_requester_id(update.effective_user.id))

    
    #open(f'{game_logic.SESSION_IMAGE_DIR}/'+str(game_logic.get_session_id_by_requester_id(update.effective_user.id))+'.png', 'rb')
    try:
        context.bot.edit_message_media(
            chat_id=update.effective_chat.id,
            message_id=procces_message.message_id,
            media=InputMediaPhoto(open(f'{game_logic.SESSION_IMAGE_DIR}/'+str(game_logic.get_session_id_by_requester_id(update.effective_user.id))+'.png', 'rb'))

        )
    except Exception as e:
        print(e)


#handler funcs

def play_with_bot_handler(update :Update, context :CallbackContext):
    global procces_message
    if read_conf.PB in update.message.text:
        send_msg(update, context, "You are playing with bot!")

        #put player in game with bot
        game_logic.start_session(update.effective_user.id, read_conf.BOT)

        buttons = [
            (KeyboardButton(1), KeyboardButton(2), KeyboardButton(3)),
            (KeyboardButton(4), KeyboardButton(5), KeyboardButton(6)),
            (KeyboardButton(7), KeyboardButton(8), KeyboardButton(9))]
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Welcome to TicTacToe bot by fedorfedka!",
            reply_markup=ReplyKeyboardMarkup(buttons)
            )
            
        game_logic.update_session_grid_png(game_logic.get_session_id_by_requester_id(update.effective_user.id))

        procces_message = context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(f'{game_logic.SESSION_IMAGE_DIR}/'+str(game_logic.get_session_id_by_requester_id(update.effective_user.id))+'.png', 'rb')
            
        )
            

def play_with_human_handler(update :Update, context :CallbackContext):
    if read_conf.PH in update.message.text:
        send_msg(update, context, 'wip')


def send_msg(update :Update, context :CallbackContext, text :str):
    """easy way to send message"""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        )

#to send photo



dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(CommandHandler('stop', stop_command))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
dispatcher.add_handler(MessageHandler(Filters.text, turns_handler))

updater.start_polling()