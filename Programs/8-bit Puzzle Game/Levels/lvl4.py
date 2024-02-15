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


character_mask = pg.mask.from_surface(pg.Surface((15, 22)))  # The surface size decides the hit-box of the player, so have fun tweaking around :)
character_sprite_sheet = pg.transform.scale(pg.image.load(
    "../../../assets/graphics/8-Bit Pixel Game/lvl4/temp_char_ss.png").convert_alpha(), (80, 104))


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

char_anim_state = 0  # Denotes whether character is going left, right, up or down
char_anim_frame = 0

key_anim_frame = 0
reverse_anim = False

# Defining Functions -------------------------------------------------------------------------------------------


def handle_key_input():
    global char_anim_state

    keys = pg.key.get_pressed()

    if keys[pg.K_s] or keys[pg.K_DOWN]:
        maze_blit_position[1] -= 5
        char_anim_state = 0

        if maze_mask.overlap(character_mask, (957 - maze_blit_position[0], 537 - maze_blit_position[1])):
            maze_blit_position[1] += 5

    if keys[pg.K_w] or keys[pg.K_UP]:
        maze_blit_position[1] += 5
        char_anim_state = 3

        if maze_mask.overlap(character_mask, (957 - maze_blit_position[0], 537 - maze_blit_position[1])):
            maze_blit_position[1] -= 5

    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        maze_blit_position[0] -= 5
        char_anim_state = 1

        if maze_mask.overlap(character_mask, (957 - maze_blit_position[0], 537 - maze_blit_position[1])) or maze_blit_position[0] <= -2240:  # Checks if player collides with maze or goes out of bounds
            maze_blit_position[0] += 5

    if keys[pg.K_a] or keys[pg.K_LEFT]:
        maze_blit_position[0] += 5
        char_anim_state = 2

        if maze_mask.overlap(character_mask, (957 - maze_blit_position[0], 537 - maze_blit_position[1])) or maze_blit_position[0] >= 970:  # Checks if player collides with maze or goes out of bounds
            maze_blit_position[0] -= 5

    if not any(keys):
        char_anim_state = -1


def check_for_player_events():  # Events refer to either finding of keys or reaching special areas within the maze

    # Key masks are the same but the offset decides whether we collided with a specific key or not
    if key_mask.overlap(character_mask, (957 - maze_blit_position[0] - 2727, 537 - maze_blit_position[1] - 581)):
        keys_obtained[0] = 1

    if key_mask.overlap(character_mask, (957 - maze_blit_position[0] - 775, 537 - maze_blit_position[1] - 1796)):
        keys_obtained[1] = 1

    if key_mask.overlap(character_mask, (957 - maze_blit_position[0] - 1590, 537 - maze_blit_position[1] - 1560)):
        keys_obtained[2] = 1

    if -2620 < maze_blit_position[1] <= -2585:
        if all(keys_obtained):
            print("Level Cleared!")
        else:
            print("You need all three keys to unlock this door")

    if -220 <= maze_blit_position[0] <= -200 and -770 <= maze_blit_position[1] <= -730:
        maze_blit_position[0] -= 5

    if -2200 >= maze_blit_position[0] and -1495 <= maze_blit_position[1] <= -1455:
        maze_blit_position[0] += 5


def draw_game_elements():
    screen.fill((100, 100, 100))

    screen.blit(maze, maze_blit_position)
    screen.blit(maze_3d_effect, (maze_blit_position[0] + 3, maze_blit_position[1]))

    if char_anim_state != -1:  # Character blitting when moving
        screen.blit(character_sprite_sheet, (957, 537), (20 * char_anim_frame, 27 * char_anim_state, 20, 26))
    else:
        screen.blit(character_sprite_sheet, (957, 537), (20, 0, 20, 26))  # Character blitting when idle

    if not keys_obtained[0]:
        screen.blit(cyan_key_sprite_sheet,
                    (maze_blit_position[0] + 2725, maze_blit_position[1] + 581),
                    (0, 41 * key_anim_frame, 33, 41))

    if not keys_obtained[1]:
        screen.blit(magenta_key_sprite_sheet,
                    (maze_blit_position[0] + 775, maze_blit_position[1] + 1796),
                    (0, 41 * key_anim_frame, 33, 41))

    if not keys_obtained[2]:
        screen.blit(yellow_key_sprite_sheet,
                    (maze_blit_position[0] + 1590, maze_blit_position[1] + 1559),
                    (0, 41 * key_anim_frame, 33, 41))


def animate_game_elements():
    global key_anim_frame, last_anim_update, reverse_anim, char_anim_state, char_anim_frame

    if pg.time.get_ticks() - last_anim_update >= 145:

        if key_anim_frame < 3 and not reverse_anim:  # Key Animation
            key_anim_frame += 1
        elif key_anim_frame != 0:
            reverse_anim = True
            key_anim_frame -= 1
        else:
            key_anim_frame = 1
            reverse_anim = False
        last_anim_update = pg.time.get_ticks()

        if char_anim_state != -1:  # Character Animation
            if char_anim_frame > 2:
                char_anim_frame = 0
            else:
                char_anim_frame += 1


# Main Loop ----------------------------------------------------------------------------------------------------

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    handle_key_input()
    check_for_player_events()

    animate_game_elements()
    draw_game_elements()

    pg.display.update()
    clock.tick(60)
