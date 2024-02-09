import pygame as pg

# Setting Up Pygame Pre-requisites -----------------------------------------------------------------------------

screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

pg.init()

# Defining Run Time Variables ----------------------------------------------------------------------------------

character_x = 500
character_y = 0

character_size_x = 35
character_size_y = 35

character_ground_level = 565

fall_velocity = 9.8 / 1000
jump_velocity = 4.9

to_jump = False

last_time_on_ground = pg.time.get_ticks()
last_time_jumped = -900

Plat1 = pg.Rect(10, 550, 100, 10)
Plat2 = pg.Rect(150, 500, 100, 10)
Plat3 = pg.Rect(290, 450, 100, 10)

Platforms = [Plat1, Plat2, Plat3]

platform_currently_under = -1

# Defining Functions -------------------------------------------------------------------------------------------


def handle_key_input():
    global character_x, character_y, to_jump
    keys = pg.key.get_pressed()

    if keys[pg.K_d]:
        character_x += 5
    if keys[pg.K_a]:
        character_x -= 5

    if keys[pg.K_SPACE] and character_y == character_ground_level:
        to_jump = True


def implement_gravity():
    global character_y, last_time_on_ground, to_jump

    frame_fall_velocity = fall_velocity * (1 + pg.time.get_ticks() - last_time_on_ground)

    if character_y >= character_ground_level and not to_jump:
        last_time_on_ground = pg.time.get_ticks()
        character_y = character_ground_level
        return

    character_y += frame_fall_velocity - to_jump * jump_velocity

    if character_y >= character_ground_level: to_jump = False


def handle_platform_collisions(plat):
    global character_y, character_x, character_ground_level, to_jump, platform_currently_under

    if plat.y - character_size_y < character_y < plat.y + plat.height:  # For ensuring that character sides don't clip
        if character_x + 35 == plat.x:                                  # through platforms
            character_x -= 5
        elif character_x == plat.x + plat.width:
            character_x += 5

    if plat.x - character_size_x < character_x < plat.x + plat.width:  # For landing on platform tops & to hit your head
        if character_y + character_size_y < plat.y:                    # on platform bottoms
            character_ground_level = plat.y - character_size_y
            platform_currently_under = Platforms.index(plat)
        elif plat.y < character_y < plat.y + plat.height:
            character_y += 5
            to_jump = not to_jump

    elif Platforms.index(plat) == platform_currently_under:
        character_ground_level = 565


def draw_elements():
    pg.draw.rect(screen, "purple", pg.Rect(character_x, character_y, 35, 35))
    for platform_to_draw in Platforms:
        pg.draw.rect(screen, "black", platform_to_draw)


# Main Loop ----------------------------------------------------------------------------------------------------

while True:
    screen.fill('white')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for platform in Platforms:
        handle_platform_collisions(platform)

    implement_gravity()
    handle_key_input()

    draw_elements()

    pg.display.update()
    clock.tick(60)
