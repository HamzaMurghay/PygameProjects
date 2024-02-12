import pygame as pg

# Setting Up Pygame Pre-requisites -----------------------------------------------------------------------------

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('../../../assets/graphics/8-Bit Pixel Game/lvl4/past_maze.png'))
clock = pg.time.Clock()

pg.init()

# Setting up Game Elements -------------------------------------------------------------------------------------

maze = pg.transform.scale(pg.image.load(
    '../../../assets/graphics/8-Bit Pixel Game/lvl4/maze.png').convert_alpha(), (2200, 2200))

maze_mask = pg.mask.from_surface(maze, 0)
maze_mask_surface = maze_mask.to_surface()


maze_3d_effect = pg.transform.scale(pg.image.load(
    '../../../assets/graphics/8-Bit Pixel Game/lvl4/maze_3D_effect.png').convert_alpha(), (2200, 2200))


character_surf = pg.transform.scale(
    pg.image.load("../../../assets/graphics/8-Bit Pixel Game/lvl4/character.png").convert_alpha(), (10, 10))

character_mask = pg.mask.from_surface(character_surf)

yellow_key = pg.transform.scale(
    pg.image.load("../../../assets/graphics/8-Bit Pixel Game/lvl4/yellow_key.png").convert_alpha(), (35, 35))
yellow_key_mask = pg.mask.from_surface(yellow_key)

sprite_sheet_yellow = pg.image.load(
    "../../../assets/graphics/8-Bit Pixel Game/lvl4/yellow_key_sprite_sheet.png").convert_alpha()

# Setting up Game Variables ------------------------------------------------------------------------------------

maze_blit_position = [-797, 350]

keys_obtained = [0, 0, 0]  # These represent whether the player got the cyan, yellow and magenta keys respectively

last_anim_update = 0
anim_frame = 0
reverse_anim = False


# Defining Functions -------------------------------------------------------------------------------------------


def handle_key_input():
    keys = pg.key.get_pressed()

    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        maze_blit_position[0] -= 5

        if maze_mask.overlap(character_mask, (300 - maze_blit_position[0], 300 - maze_blit_position[1])):
            maze_blit_position[0] += 5

    if keys[pg.K_a] or keys[pg.K_LEFT]:
        maze_blit_position[0] += 5

        if maze_mask.overlap(character_mask, (300 - maze_blit_position[0], 300 - maze_blit_position[1])):
            maze_blit_position[0] -= 5

    if keys[pg.K_s] or keys[pg.K_DOWN]:
        maze_blit_position[1] -= 5

        if maze_mask.overlap(character_mask, (300 - maze_blit_position[0], 300 - maze_blit_position[1])):
            maze_blit_position[1] += 5

    if keys[pg.K_w] or keys[pg.K_UP]:
        maze_blit_position[1] += 5

        if maze_mask.overlap(character_mask, (300 - maze_blit_position[0], 300 - maze_blit_position[1])):
            maze_blit_position[1] -= 5

    if keys[pg.K_RETURN]:
        print("\nCurrent Position: ", maze_blit_position)
        maze_blit_position[0], maze_blit_position[1] = map(int, input("Enter Teleport co-ords: ").split())


def check_key_gotten():
    if yellow_key_mask.overlap(character_mask,
                               (300 - maze_blit_position[0] - 1087, 300 - maze_blit_position[1] - 1072)):
        keys_obtained[1] = 1


def draw_game_elements():
    screen.fill((100, 100, 100))

    screen.blit(maze, maze_blit_position)
    screen.blit(maze_3d_effect, (maze_blit_position[0] + 3, maze_blit_position[1]))

    screen.blit(character_surf, (300, 300))
    if not keys_obtained[1]: screen.blit(yellow_key, (maze_blit_position[0] + 1087, maze_blit_position[1] + 1072))

    screen.blit(sprite_sheet_yellow, (0, 0), (0, 41*anim_frame, 33, 41))


def animate_keys():
    global anim_frame, last_anim_update, reverse_anim

    if pg.time.get_ticks() - last_anim_update >= 145:
        if anim_frame < 3 and not reverse_anim:
            anim_frame += 1
        elif anim_frame != 0:
            reverse_anim = True
            anim_frame -= 1
        else:
            anim_frame = 1
            reverse_anim = False
        last_anim_update = pg.time.get_ticks()


# Main Loop ----------------------------------------------------------------------------------------------------

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    handle_key_input()
    check_key_gotten()
    animate_keys()

    draw_game_elements()

    pg.display.update()
    clock.tick(60)
