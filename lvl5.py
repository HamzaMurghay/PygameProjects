import pygame as pg
import random

# Setting up Pygame Base Objects ----------------------------------------------------------------------

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('graphics/8-Bit Pixel Game/back_arrow.png'))  # Change this
screen.fill('darkgrey')
clock = pg.time.Clock()

pg.init()

font = pg.font.SysFont('Consolas', 90)

# Creating assets -------------------------------------------------------------------------------------

click_cursor = pg.image.load('graphics/8-Bit Pixel Game/Pointing_hand_cursor.svg.png').convert_alpha()
change_mouse = False

# Function Definitions --------------------------------------------------------------------------------


def update_lights():
    light_line1 = font.render(f"{' '.join(str(l) for l in lights[0:4])}", True, 'black')
    light_line2 = font.render(f"{' '.join(str(l) for l in lights[4:8])}", True, 'black')
    light_line3 = font.render(f"{' '.join(str(l) for l in lights[8:12])}", True, 'black')
    light_line4 = font.render(f"{' '.join(str(l) for l in lights[12:16])}", True, 'black')

    screen.blit(light_line1, (55, 95))
    screen.blit(light_line2, (55, 195))
    screen.blit(light_line3, (55, 295))
    screen.blit(light_line4, (55, 395))


def check_for_light_press():
    if (event.type == pg.KEYUP and event.key == pg.K_1) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(79, 104, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[0]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_2) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(177, 104, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[1]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_3) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(275, 104, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[2]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_4) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(373, 104, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[3]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_5) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(79, 204, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[4]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_6) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(177, 204, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[5]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_7) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(275, 204, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[6]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_8) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(373, 204, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[7]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_9) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(79, 304, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[8]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_0) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(177, 304, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[9]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_q) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(275, 304, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[10]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_w) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(373, 304, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[11]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_e) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(79, 404, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[12]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_r) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(177, 404, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[13]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_t) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(275, 404, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[14]:
            lights[light] = int(not lights[light])

    if (event.type == pg.KEYUP and event.key == pg.K_y) or (
            event.type == pg.MOUSEBUTTONUP and pg.Rect(373, 404, 42, 58).collidepoint(pg.mouse.get_pos())):
        for light in temp_all[15]:
            lights[light] = int(not lights[light])


# Setting up Program Variables ------------------------------------------------------------------------

lights = [0]*16
starting_configurations = [(4, 8, 11), (1, 6, 9), (0, 5, 8, 11), (3, 5, 13), (0, 6)]

for config in starting_configurations[random.randint(0, 4)]: lights[config] = 1


first_seq = [1, 4, 7, 10, 13, 16]
second_seq = [2, 5, 8, 11, 14]
third_seq = [3, 6, 9, 12, 15]

temp_all = [
    [(0+num) % 16 for num in first_seq if first_seq.index(num) != 0],
    [(1+num) % 16 for num in second_seq if second_seq.index(num) != 0],
    [(2+num) % 16 for num in third_seq if third_seq.index(num) != 0],

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
        check_for_light_press()

    screen.fill('darkgrey')
    update_lights()

    pg.display.update()
    clock.tick(60)


# Printing Light Mapping Matrix: ----------------------------------------------------------------------


# for light_list in temp_all:
#     matrix_row = [0]*16
#     for light_no in light_list:
#         matrix_row[light_no] = 1
#     for e in matrix_row:
#         print(e,end = " ")
#     print()
