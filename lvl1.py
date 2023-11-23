import pygame as pg

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('graphics/8-Bit Pixel Game/back_arrow.png'))  # Change this
screen.fill('darkgrey')

pg.init()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
