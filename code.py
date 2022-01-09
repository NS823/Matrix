# прошу присоедениться на сервер Discord: https://discord.gg/KKsZSdS5jk
# youtube туториал (не мой): https://www.youtube.com/watch?v=XW_2KXxw2RQ&t

import os
import pygame as pg
from random import choice, randrange

class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_katakana)
        self.interval = randrange(5, 30)


    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_katakana if color == 'green' else lightgreen_katakana)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surfase.blit(self.value, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(8, 18)
        self.speed = randrange(2, 6)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]


os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1600, 900
FONT_SIZE = 40
alpha_value = 50

pg.init()
screen = pg.display.set_mode(RES)
surfase = pg.Surface(RES)
surfase.set_alpha(alpha_value)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.SysFont('Yu Gothic', FONT_SIZE, bold=True)
green_katakana = [font.render(char, True, (0, randrange(160, 256), 0)) for char in katakana]
lightgreen_katakana = [font.render(char, True, pg.Color('lightgreen')) for char in katakana]


symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]


while True:
    screen.blit(surfase, (0, 0))
    surfase.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60)
