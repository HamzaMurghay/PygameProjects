import pygame as pg

screen = pg.display.set_mode((1080, 700))
pg.display.set_caption("Elemental Game")
clock = pg.time.Clock()

pg.init()

character_position = pg.Vector2(0, 0)
character_direction = pg.Vector2(0, 0)


def handle_key_input():
    keys = pg.key.get_pressed()

    # if keys[pg.K_w]:
    #     character_position.y -= 5
    # if keys[pg.K_a]:
    #     character_position.x -= 5
    #
    # if keys[pg.K_s]:
    #     character_position.y += 5
    #
    # if keys[pg.K_d]:
    #     character_position.x += 5

    if keys[pg.K_SPACE]:
        character_position.x += 5*character_direction.x
        character_position.y += 5*character_direction.y


while True:
    screen.fill('white')
    mouse_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    character_direction += pg.Vector2(mouse_pos[0], mouse_pos[1]).normalize()
    character_direction = character_direction.normalize()

    handle_key_input()

    pg.draw.rect(screen, 'red', pg.Rect(*character_position, 35, 35))

    pg.display.update()
    clock.tick(60)
