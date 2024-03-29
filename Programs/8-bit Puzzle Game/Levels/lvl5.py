import pygame as pg
import random

# Setting up Pygame Base Objects -------------------------------------------------------------------------------

screen = pg.display.set_mode((1920, 1080))
pg.display.set_icon(pg.image.load('../../../assets/graphics/8-Bit Pixel Game/main_code/back_arrow.png'))  # Change this
clock = pg.time.Clock()

pg.init()

# Creating assets and Related Variables ------------------------------------------------------------------------

light_on = pg.transform.scale(pg.image.load(
    '../../../assets/graphics/8-Bit Pixel Game/lvl5/light_on.png').convert_alpha(), (60, 80))
light_off = pg.transform.scale(pg.image.load(
    '../../../assets/graphics/8-Bit Pixel Game/lvl5/light_off.png').convert_alpha(), (60, 80))

light_state = [light_off, light_on]

click_cursor = pg.image.load(
    '../../../assets/graphics/8-Bit Pixel Game/main_code/Pointing_hand_cursor.svg.png').convert_alpha()
change_mouse = False

# Function Definitions -----------------------------------------------------------------------------------------


def display_light_grid(light_list):
    light_grid = [light_state[light] for light in light_list]
    light_grid_positions = [(610+current_column_y*213, 180+current_row_x*213) for current_row_x in range(4) for current_column_y in range(4)]

    screen.blits(
        [(surface, position) for surface, position in zip(light_grid, light_grid_positions)]
    )


def change_light_list(light_clicked):
    for light in list_of_mappings[light_clicked]:
        lights[light] = int(not lights[light])


def check_for_cursor_hover_and_click(click_event):
    for row_no in range(4):
        for column_no in range(4):

            if pg.Rect(610+(row_no*213), 180+(column_no*213), 60, 80).collidepoint(pg.mouse.get_pos()):
                pg.mouse.set_visible(False)
                if click_event.type == pg.MOUSEBUTTONUP:
                    change_light_list(row_no + column_no * 4)  # Getting the current list element address using only its row and column number by use of the formula current_row_number * size of grid + current_column_number
                return True

    pg.mouse.set_visible(True)
    return False


# Setting up Program Variables ------------------------------------------------------------------------

lights = [0] * 16
starting_configurations = [(4, 8, 11), (1, 6, 9), (0, 5, 8, 11), (3, 5, 13), (0, 6)]

for config in starting_configurations[random.randint(0, 4)]:
    lights[config] = 1

first_seq = [1, 4, 7, 10, 13, 16]
second_seq = [2, 5, 8, 11, 14]
third_seq = [3, 6, 9, 12, 15]

list_of_mappings = [
    [(0 + num) % 16 for num in first_seq if first_seq.index(num) != 0],
    [(1 + num) % 16 for num in second_seq if second_seq.index(num) != 0],
    [(2 + num) % 16 for num in third_seq if third_seq.index(num) != 0],

    [(3 + num) % 16 for num in first_seq if first_seq.index(num) != 1],
    [(4 + num) % 16 for num in second_seq if second_seq.index(num) != 1],
    [(5 + num) % 16 for num in third_seq if third_seq.index(num) != 1],

    [(6 + num) % 16 for num in first_seq if first_seq.index(num) != 2],
    [(7 + num) % 16 for num in second_seq if second_seq.index(num) != 2],
    [(8 + num) % 16 for num in third_seq if third_seq.index(num) != 2],

    [(9 + num) % 16 for num in first_seq if first_seq.index(num) != 3],
    [(10 + num) % 16 for num in second_seq if second_seq.index(num) != 3],
    [(11 + num) % 16 for num in third_seq if third_seq.index(num) != 3],

    [(12 + num) % 16 for num in first_seq if first_seq.index(num) != 4],
    [(13 + num) % 16 for num in second_seq if second_seq.index(num) != 4],
    [(14 + num) % 16 for num in third_seq if third_seq.index(num) != 4],

    [(15 + num) % 16 for num in first_seq if first_seq.index(num) != 5],
]

# Main Loop -------------------------------------------------------------------------------------------

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        change_mouse = check_for_cursor_hover_and_click(event)

    screen.fill('purple')
    display_light_grid(lights)

    mouse_pos = pg.mouse.get_pos()

    if change_mouse:
        screen.blit(click_cursor, (mouse_pos[0] - 15, mouse_pos[1]))

    screen.blit(light_on, (0, 0))
    print(mouse_pos)

    pg.display.update()
    clock.tick(60)
