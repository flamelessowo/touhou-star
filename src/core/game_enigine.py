import pygame
import pygame as pg


class Game:
    done = False

    def __init__(self, width, height) -> None:
        pg.init()
        pg.display.set_mode((width, height))
        pg.display.set_caption('Touhou *')
        self.clock = pg.time.Clock()

    def run(self) -> None:
        while not self.done:
            for event in pg.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            pygame.display.flip()
