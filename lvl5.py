import pygame as pg
import random

# Setting up Pygame Base Objects ----------------------------------------------------------------------

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('graphics/8-Bit Pixel Game/back_arrow.png'))  # Change this
clock = pg.time.Clock()

pg.init()

font = pg.font.SysFont('Consolas', 90)

# Creating assets -------------------------------------------------------------------------------------

click_cursor = pg.image.load('graphics/8-Bit Pixel Game/Pointing_hand_cursor.svg.png').convert_alpha()
change_mouse = False


# Function Definitions --------------------------------------------------------------------------------


def update_lights(light_list):
    light_line1 = font.render(f"{' '.join(str(l) for l in light_list[0:4])}", True, 'black')
    light_line2 = font.render(f"{' '.join(str(l) for l in light_list[4:8])}", True, 'black')
    light_line3 = font.render(f"{' '.join(str(l) for l in light_list[8:12])}", True, 'black')
    light_line4 = font.render(f"{' '.join(str(l) for l in light_list[12:16])}", True, 'black')

    screen.blit(light_line1, (115, 95))
    screen.blit(light_line2, (115, 195))
    screen.blit(light_line3, (115, 295))
    screen.blit(light_line4, (115, 395))


def check_for_light_press(mapping_list, light_list):
    global change_mouse

    if pg.Rect(119, 104, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(217, 104, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(315, 104, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(413, 104, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(119, 204, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(217, 204, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(315, 204, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(413, 204, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(119, 304, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(217, 304, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(315, 304, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(413, 304, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(119, 404, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(217, 404, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(315, 404, 42, 58).collidepoint(pg.mouse.get_pos()) or \
            pg.Rect(413, 404, 42, 58).collidepoint(pg.mouse.get_pos()):

        pg.mouse.set_visible(False)
        change_mouse = True
    else:
        pg.mouse.set_visible(True)
        change_mouse = False

    if event.type == pg.MOUSEBUTTONUP and pg.Rect(119, 104, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[0]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(217, 104, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[1]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(315, 104, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[2]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(413, 104, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[3]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(119, 204, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[4]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(217, 204, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[5]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(315, 204, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[6]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(413, 204, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[7]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(119, 304, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[8]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(217, 304, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[9]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(315, 304, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[10]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(413, 304, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[11]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(119, 404, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[12]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(217, 404, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[13]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(315, 404, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[14]:
            light_list[light] = int(not light_list[light])

    elif event.type == pg.MOUSEBUTTONUP and pg.Rect(413, 404, 42, 58).collidepoint(pg.mouse.get_pos()):
        for light in mapping_list[15]:
            light_list[light] = int(not light_list[light])


# Setting up Program Variables ------------------------------------------------------------------------

lights = [0] * 16
starting_configurations = [(4, 8, 11), (1, 6, 9), (0, 5, 8, 11), (3, 5, 13), (0, 6)]

for config in starting_configurations[random.randint(0, 4)]: lights[config] = 1


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
        check_for_light_press(list_of_mappings, lights)

    screen.fill('darkgrey')
    update_lights(lights)

    if change_mouse:
        screen.blit(click_cursor, (pg.mouse.get_pos()[0] - 15, pg.mouse.get_pos()[1]))

    pg.display.update()
    clock.tick(60)

# EXTRA STUFF:

# 1) Printing Light Mapping Matrix: ----------------------------------------------------------------------


# for light_list in temp_all:
#     matrix_row = [0]*16
#     for light_no in light_list:
#         matrix_row[light_no] = 1
#     for e in matrix_row:
#         print(e,end = " ")
#     print()

# IMPORTANT!!! ----------------------------------------------------------------------------------------

# 2) This is how to generate algorithms until sum of n keys:

# Algorithm for sum of 2 keys:

# for light_mapping_list in temp_all:
#     for i in range(temp_all.index(light_mapping_list)+1, 16):
#         for pos in light_mapping_list:
#             lights[pos] = int(not lights[pos])
#         for second_operand_pos in temp_all[i]:
#             lights[second_operand_pos] = int(not lights[second_operand_pos])
#         if lights.count(1) <= 3: print(f"Lights after {temp_all.index(light_mapping_list) + 1} + {i+1} = {lights}")
#         lights = [0]*16


# Algorithm for sum of 3 keys:

# for light_mapping_list in temp_all:
#     for i in range(temp_all.index(light_mapping_list)+1, 16):
#         for j in range(temp_all.index(light_mapping_list) + 1, 16):
#             for pos in light_mapping_list:
#                 lights[pos] = int(not lights[pos])
#             for second_operand_pos in temp_all[i]:
#                 lights[second_operand_pos] = int(not lights[second_operand_pos])
#             for third_operand_pos in temp_all[j]:
#                 lights[third_operand_pos] = int(not lights[third_operand_pos])
#             if lights.count(1) <= 3:
#                 print(f"Lights after {temp_all.index(light_mapping_list) + 1} + {i+1} + {j+1} = {lights}")
#             lights = [0]*16

# Algorithm for sum of 4 keys:

# for light_mapping_list in temp_all:
#     for i in range(temp_all.index(light_mapping_list)+1, 16):
#         for j in range(temp_all.index(light_mapping_list) + 1, 16):
#             for k in range(temp_all.index(light_mapping_list) + 1, 16):
#                 for pos in light_mapping_list:
#                     lights[pos] = int(not lights[pos])
#                 for second_operand_pos in temp_all[i]:
#                     lights[second_operand_pos] = int(not lights[second_operand_pos])
#                 for third_operand_pos in temp_all[j]:
#                     lights[third_operand_pos] = int(not lights[third_operand_pos])
#                 for fourth_operand_pos in temp_all[k]:
#                     lights[fourth_operand_pos] = int(not lights[fourth_operand_pos])
#                 if lights.count(1) <= 3:
#                     print(f"Lights after {temp_all.index(light_mapping_list) + 1} + {i+1} + {j+1} + {k+1} = {lights}")
#                 lights = [0]*16

# As you can see there is a pattern to this algorithm, so it is easy for you to extend it to higher sums, just be sure
# to have enough computer power :P (most max out at 7)

# ALGORITHM FOR 6 KEYS:   [I absolutely LOVE this algo, it's so OP, like forget getting 2 key flipped cases(not that those aren't good, they're AMAZING but), you can literally solve the whole puzzle by putting in your state]

# for light_mapping_list in temp_all:
#     for i in range(temp_all.index(light_mapping_list)+1, 16):
#         for j in range(temp_all.index(light_mapping_list) + 1, 16):
#             for k in range(temp_all.index(light_mapping_list) + 1, 16):
#                 for l in range(temp_all.index(light_mapping_list) + 1, 16):
#                     for m in range(temp_all.index(light_mapping_list) + 1, 16):
#                             for pos in light_mapping_list:
#                                 lights[pos] = int(not lights[pos])
#                             for second_operand_pos in temp_all[i]:
#                                 lights[second_operand_pos] = int(not lights[second_operand_pos])
#                             for third_operand_pos in temp_all[j]:
#                                 lights[third_operand_pos] = int(not lights[third_operand_pos])
#                             for fourth_operand_pos in temp_all[k]:
#                                 lights[fourth_operand_pos] = int(not lights[fourth_operand_pos])
#                             for fifth_operand_pos in temp_all[l]:
#                                 lights[fifth_operand_pos] = int(not lights[fifth_operand_pos])
#                             for sixth_operand_pos in temp_all[m]:
#                                 lights[sixth_operand_pos] = int(not lights[sixth_operand_pos])
#                             if lights == [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
#                                 print(f"Lights after {temp_all.index(light_mapping_list) + 1} + {i+1} + {j+1} + {k+1} + {l+1} + {m+1} = {lights}")
#                             lights = [0]*16


# Solution for (0,6):
#
# 5 steps: 1 + 2 + 3 + 8 + 16 (found using above algo, 5th variant in 2 sec)
#
# 6 steps: 1 + 3 + 5 + 11 + 14 + 16 (found using above algo in 13 sec)
