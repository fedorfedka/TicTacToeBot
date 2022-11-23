import json

conf :dict
with open('conf.json', 'r') as file:
    conf = json.load(file)

TOKEN :str = conf['token']
PB :str = conf['game_options'][0]
PH :str = conf['game_options'][1]
DATABASE :str = conf['database_name']
BOT :str = conf['bot']