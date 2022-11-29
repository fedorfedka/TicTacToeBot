from PIL import Image, ImageChops
import json
import random


EMPTY_SYM = '[]'
X_SYM = 'x'
O_SYM = 'o'
SOURCE_IMAGE_DIR = './image/source_image'
SESSION_IMAGE_DIR = './image/session_image'

def create_session_list():
    with open('sess.json', 'w') as file:
        file.write(json.dumps({}))


def start_session(requester_id :str, accepter_id :str):
    is_requester_turn = bool(random.randint(0,1))
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for i in range(1, 101):
            if str(i) not in all_sess:
                all_sess[i] = [
                    requester_id,
                    accepter_id,
                    is_requester_turn,
                    {"cells": (
                        (EMPTY_SYM, EMPTY_SYM, EMPTY_SYM),
                        (EMPTY_SYM, EMPTY_SYM, EMPTY_SYM),
                        (EMPTY_SYM, EMPTY_SYM, EMPTY_SYM)
                    )}
                ]
                update_session_grid_png(i)
                break

    with open('sess.json', 'w') as file:
        file.write(json.dumps(all_sess))


def edit_session_grid(session_id :str, row :int, column :int):
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for key, elem in all_sess.items():
            if session_id in key and all_sess[key][3]['cells'][row][column] == EMPTY_SYM:

                all_sess[key][3]['cells'][row][column] = X_SYM if get_session_turn(session_id) else O_SYM
                all_sess[key][2] = False if get_session_turn(session_id) else True

                break
    
    next_turn(session_id)


    with open('sess.json', 'w') as file:
        file.write(json.dumps(all_sess))


def next_turn(session_id :str):
    if get_session_turn(session_id):
        set_session_turn(session_id, False)
    
    else:
        set_session_turn(session_id, True)


def delete_session_by_requester(requester_id :str):
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for key, elem in all_sess.items():
            if requester_id in elem:
                all_sess.pop(key)
                break
    
    with open('sess.json', 'w') as file:
        file.write(json.dumps(all_sess))


def is_requester_in_game(requester_id :str) -> bool:
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for key, elem in all_sess.items():
            if requester_id in elem:
                return True

    return False


def get_session_turn(session_id :str) -> bool:
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for key, elem in all_sess.items():
            if session_id in key:
                return elem[2]


def set_session_turn(session_id :str, turn :bool):
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for key, elem in all_sess.items():
            if session_id in key:
                all_sess[key][2] = turn
                break
    
    with open('sess.json', 'w') as file:
        file.write(json.dumps(all_sess))


def update_session_grid_png(session_id :str):
    with Image.open(f'{SOURCE_IMAGE_DIR}/grid.png') as grid_png:
        all_sess :dict
        with open('sess.json') as file:
            all_sess = json.load(file)
            for key, elem in all_sess.items():
                if key == session_id:
                    for row in range(3):
                        for column in range(3):
                            #print(elem[3]['cells'][row][column])
                            if elem[3]['cells'][row][column] == X_SYM:
                                #print(True)
                                with Image.open(f"{SOURCE_IMAGE_DIR}/x/{row}_{column}.png") as xe:
                                    grid_png = Image.alpha_composite(grid_png, xe)
                            
                            if elem[3]['cells'][row][column] == O_SYM:
                                #print(True)
                                with Image.open(f"{SOURCE_IMAGE_DIR}/o/{row}_{column}.png") as xe:
                                    grid_png = Image.alpha_composite(grid_png, xe)
                        


        grid_png.save(f'{SESSION_IMAGE_DIR}/{session_id}.png')


def get_session_id_by_requester_id(requester_id :str) -> str:
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for key, elem in all_sess.items():
            if int(requester_id) in elem:
                return key

    return ''

def get_cell(session_id, row, column) -> str:
    all_sess :dict
    with open('sess.json') as file:
        all_sess = json.load(file)
        for key, elem in all_sess.items():
            if session_id in key:
                return elem[3]['cells'][row][column]

    return ''


def is_cell_empty(session_id, row, column) -> bool:
    if get_cell(session_id, row, column) == EMPTY_SYM:
        return True
    
    return False
    

def random_empty_cell(session_id):
    row, column = random.randint(0, 2), random.randint(0,2)
    while True:
        if is_cell_empty(session_id, row, column):
            break
        else:
            row, column = random.randint(0, 2), random.randint(0,2)

    return row, column


def bot_turn(session_id):
    if get_session_turn(session_id) == False:
        row, column = random_empty_cell(session_id)
        edit_session_grid(session_id, row, column)
