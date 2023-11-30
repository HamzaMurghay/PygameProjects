import pygame as pg

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('../graphics/8-Bit Pixel Game/back_arrow.png'))  # Change this
clock = pg.time.Clock()

pg.init()

maze1 = pg.image.lo

character_x = 100
character_y = 100


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        character_x += 5
    if keys[pg.K_a]:
        character_x -= 5
    if keys[pg.K_s]:
        character_y += 5
    if keys[pg.K_w]:
        character_y -= 5

    if character_x > 600:
        character_x = -35
    elif character_x < -35:
        character_x = 600
    elif character_y < -40:
        character_y = 630
    elif character_y > 630:
        character_y = -30

    screen.fill('darkgrey')
    boundary = pg.draw.rect(screen, 'blue', pg.Rect(20, 20, 200, 200))

    line = pg.draw.line(screen, 'black', (200,  200), (200, 300))

    character = pg.draw.rect(screen, 'red', pg.Rect(character_x, character_y, 35, 35))
    character_left = pg.draw.line(screen, 'red', character.topleft, character.bottomleft)
    character_right = pg.draw.line(screen, 'red', character.topright, character.bottomright)
    character_top = pg.draw.line(screen, 'red', character.topleft, character.topright)
    character_bottom = pg.draw.line(screen, 'red', character.bottomleft, character.bottomright)

    if character_left.collideobjects([line]): character_x += 5
    if character_right.collideobjects([line]): character_x -= 5
    if character_top.collideobjects([line]): character_y += 5
    if character_bottom.collideobjects([line]): character_y -= 5

    pg.display.update()
    clock.tick(60)
