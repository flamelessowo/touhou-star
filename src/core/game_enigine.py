import pygame as pg
from src.helpers import json_helper

config = json_helper.read_config('../../settings/config.json', 'window')


class Game:
    def __init__(self) -> None:
        pg.init()
        pg.display.set_mode(config['width'], config['height'])

    def run(self) -> None:
        pass
