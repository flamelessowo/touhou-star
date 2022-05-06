from core.game_enigine import Game
from helpers.json_helper import read_config

config = read_config('../settings/config.json')
window = config['window']
game = Game(window['width'], window['height'])
game.run()
