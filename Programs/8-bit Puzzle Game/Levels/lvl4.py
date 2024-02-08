import pygame as pg

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('../../../assets/graphics/8-Bit Pixel Game/lvl4/maze_original.png'))  # Change this
clock = pg.time.Clock()

pg.init()

maze1 = pg.image.load('../../../assets/graphics/8-Bit Pixel Game/lvl4/maze.png').convert_alpha()
maze1 = pg.transform.scale(maze1, (900, 900))
maze_mask = pg.mask.from_surface(maze1, 0)
maze_mask_surface = maze_mask.to_surface()

character_surf = pg.transform.scale(
    pg.image.load("../../../assets/graphics/8-Bit Pixel Game/lvl4/character.png").convert_alpha(), (10, 10))
character_mask = pg.mask.from_surface(character_surf)
character_rect = character_surf.get_rect(topleft=(350, 5))


def handle_key_input():
    keys = pg.key.get_pressed()

    if keys[pg.K_d]:
        character_rect.x += 5
    if keys[pg.K_a]:
        character_rect.x -= 5
    if keys[pg.K_s]:
        character_rect.y += 5
    if keys[pg.K_w]:
        character_rect.y -= 5


def draw_game_elements():
    screen.fill('darkgrey')
    screen.blit(maze_mask_surface, (0, 0))
    screen.blit(character_surf, character_rect)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    handle_key_input()
    draw_game_elements()

    pg.display.update()
    clock.tick(60)
