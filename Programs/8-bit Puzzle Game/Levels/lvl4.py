import pygame as pg

# Setting Up Pygame Pre-requisites -----------------------------------------------------------------------------

screen = pg.display.set_mode((1920, 1080))
pg.display.set_icon(pg.image.load('../../../assets/graphics/8-Bit Pixel Game/lvl4/past_maze.png'))
clock = pg.time.Clock()

pg.init()

# Setting up Game Elements -------------------------------------------------------------------------------------

maze = pg.transform.scale(pg.image.load(
    '../../../assets/graphics/8-Bit Pixel Game/lvl4/maze.png').convert_alpha(), (3200, 3200))

maze_mask = pg.mask.from_surface(maze, 0)
maze_mask_surface = maze_mask.to_surface()

maze_3d_effect = pg.transform.scale(pg.image.load(
    '../../../assets/graphics/8-Bit Pixel Game/lvl4/maze_3D_effect.png').convert_alpha(), (3200, 3200))

character_surf = pg.transform.scale(
    pg.image.load("../../../assets/graphics/8-Bit Pixel Game/lvl4/character.png").convert_alpha(), (15, 20))
character_mask = pg.mask.from_surface(character_surf)

character_sprite_sheet = pg.image.load(
    "../../../assets/graphics/8-Bit Pixel Game/lvl4/temp_character_sprite_sheet.png").convert_alpha()

yellow_key = pg.transform.scale(
    pg.image.load("../../../assets/graphics/8-Bit Pixel Game/lvl4/yellow_key.png").convert_alpha(), (35, 35))

yellow_key_sprite_sheet = pg.image.load(
    "../../../assets/graphics/8-Bit Pixel Game/lvl4/yellow_key_sprite_sheet.png").convert_alpha()

cyan_key_sprite_sheet = pg.image.load(
    "../../../assets/graphics/8-Bit Pixel Game/lvl4/cyan_key_sprite_sheet.png").convert_alpha()

magenta_key_sprite_sheet = pg.image.load(
    "../../../assets/graphics/8-Bit Pixel Game/lvl4/magenta_key_sprite_sheet.png").convert_alpha()

key_mask = pg.mask.from_surface(yellow_key)  # Using the same mask to detect all keys cuz they have identical hit-boxes

# Setting up Game Variables ------------------------------------------------------------------------------------

maze_blit_position = [-640, 575]

keys_obtained = [0, 0, 0]  # These represent whether the player got the cyan, magenta and yellow keys respectively

last_anim_update = 0
anim_frame = 0
reverse_anim = False


# Defining Functions -------------------------------------------------------------------------------------------


def handle_key_input():
    keys = pg.key.get_pressed()

    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        maze_blit_position[0] -= 5

        if maze_mask.overlap(character_mask, (960 - maze_blit_position[0], 540 - maze_blit_position[1])) or maze_blit_position[0] <= -2235:  # Checks if player collides with maze or goes out of bounds
            maze_blit_position[0] += 5

    if keys[pg.K_a] or keys[pg.K_LEFT]:
        maze_blit_position[0] += 5

        if maze_mask.overlap(character_mask, (960 - maze_blit_position[0], 540 - maze_blit_position[1])) or maze_blit_position[0] >= 970:  # Checks if player collides with maze or goes out of bounds
            maze_blit_position[0] -= 5

    if keys[pg.K_s] or keys[pg.K_DOWN]:
        maze_blit_position[1] -= 5

        if maze_mask.overlap(character_mask, (960 - maze_blit_position[0], 540 - maze_blit_position[1])):
            maze_blit_position[1] += 5

    if keys[pg.K_w] or keys[pg.K_UP]:
        maze_blit_position[1] += 5

        if maze_mask.overlap(character_mask, (960 - maze_blit_position[0], 540 - maze_blit_position[1])):
            maze_blit_position[1] -= 5

    if keys[pg.K_RETURN]:
        print("\nCurrent Position: ", maze_blit_position)
        maze_blit_position[0], maze_blit_position[1] = map(int, input("Enter Teleport co-ords: ").split())


def check_if_keys_obtained():
    if key_mask.overlap(character_mask, (960 - maze_blit_position[0] - 2727, 540 - maze_blit_position[1] - 583)):  # Key masks are the same but the offset decides whether we collided with key or not
        keys_obtained[0] = 1

    if key_mask.overlap(character_mask, (960 - maze_blit_position[0] - 775, 540 - maze_blit_position[1] - 1796)):
        keys_obtained[1] = 1

    if key_mask.overlap(character_mask,(960 - maze_blit_position[0] - 1590, 540 - maze_blit_position[1] - 1564)):
        keys_obtained[2] = 1

    if -2620 < maze_blit_position[1] <= -2585:
        if all(keys_obtained):
            print("Level Cleared!")
        else:
            print("You need all three keys to unlock this door")


def draw_game_elements():
    screen.fill((100, 100, 100))

    screen.blit(maze, maze_blit_position)
    screen.blit(maze_3d_effect, (maze_blit_position[0] + 3, maze_blit_position[1]))

    screen.blit(character_surf, (960, 540))

    if not keys_obtained[0]:
        screen.blit(cyan_key_sprite_sheet,
                    (maze_blit_position[0] + 2725, maze_blit_position[1] + 581),
                    (0, 41 * anim_frame, 33, 41))

    if not keys_obtained[1]:
        screen.blit(magenta_key_sprite_sheet,
                    (maze_blit_position[0] + 775, maze_blit_position[1] + 1796),
                    (0, 41 * anim_frame, 33, 41))

    if not keys_obtained[2]:
        screen.blit(yellow_key_sprite_sheet,
                    (maze_blit_position[0] + 1590, maze_blit_position[1] + 1559),
                    (0, 41 * anim_frame, 33, 41))


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
    check_if_keys_obtained()

    animate_keys()
    draw_game_elements()

    pg.display.update()
    clock.tick(60)

# TP to Cyan Key: -1855 -100
# TP to Magenta Key: 250 -1250
# TP to Yellow Key: -640 -1000
# TP to Exit Door: -645 -2580
