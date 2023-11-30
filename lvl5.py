import pygame as pg
import random

# Setting up Pygame Base Objects ----------------------------------------------------------------------

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('graphics/8-Bit Pixel Game/back_arrow.png'))  # Change this
clock = pg.time.Clock()

pg.init()

# Creating assets -------------------------------------------------------------------------------------

light_on = pg.transform.scale(pg.image.load('graphics/8-Bit Pixel Game/lvl5/light_on.png'), (60, 80))
light_off = pg.transform.scale(pg.image.load('graphics/8-Bit Pixel Game/lvl5/light_off.png'), (60, 80))

light_state = [light_off, light_on]

click_cursor = pg.image.load('graphics/8-Bit Pixel Game/Pointing_hand_cursor.svg.png').convert_alpha()
change_mouse = False

# Function Definitions --------------------------------------------------------------------------------


def display_light_grid(light_list):
    light_grid = [light_state[light] for light in light_list]
    light_grid_positions = [(55+current_column_y*140, 30+current_row_x*140) for current_row_x in range(4) for current_column_y in range(4)]

    screen.blits(
        [(surface, position) for surface, position in zip(light_grid, light_grid_positions)]
    )


def change_light_list(light_clicked):
    for light in list_of_mappings[light_clicked]:
        lights[light] = int(not lights[light])


def check_for_cursor_hover_and_click(click_event):
    for row_no in range(4):
        for column_no in range(4):

            if pg.Rect(55+(row_no*140), 30+(column_no*140), 60, 80).collidepoint(pg.mouse.get_pos()):
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

    if change_mouse:
        screen.blit(click_cursor, (pg.mouse.get_pos()[0] - 15, pg.mouse.get_pos()[1]))

    pg.display.update()
    clock.tick(60)

# EXTRA STUFF:

# 1) Printing Light Mapping Matrix: ----------------------------------------------------------------------


# for light_list in list_of_mappings:
#     matrix_row = [0]*16
#     for light_no in light_list:
#         matrix_row[light_no] = 1
#     for e in matrix_row:
#         print(e,end = " ")
#     print()

# IMPORTANT!!! ----------------------------------------------------------------------------------------

# 2) This is how to generate algorithms until sum of n keys:

# Algorithm for sum of 2 keys:

# for light_mapping_list in list_of_mappings:
#     for i in range(list_of_mappings.index(light_mapping_list)+1, 16):
#         for pos in light_mapping_list:
#             lights[pos] = int(not lights[pos])
#         for second_operand_pos in list_of_mappings[i]:
#             lights[second_operand_pos] = int(not lights[second_operand_pos])
#         if lights.count(1) <= 3: print(f"Lights after {list_of_mappings.index(light_mapping_list) + 1} + {i+1} = {lights}")
#         lights = [0]*16


# Algorithm for sum of 3 keys:

# for light_mapping_list in list_of_mappings:
#     for i in range(list_of_mappings.index(light_mapping_list)+1, 16):
#         for j in range(list_of_mappings.index(light_mapping_list) + 1, 16):
#             for pos in light_mapping_list:
#                 lights[pos] = int(not lights[pos])
#             for second_operand_pos in list_of_mappings[i]:
#                 lights[second_operand_pos] = int(not lights[second_operand_pos])
#             for third_operand_pos in list_of_mappings[j]:
#                 lights[third_operand_pos] = int(not lights[third_operand_pos])
#             if lights.count(1) <= 3:
#                 print(f"Lights after {list_of_mappings.index(light_mapping_list) + 1} + {i+1} + {j+1} = {lights}")
#             lights = [0]*16

# Algorithm for sum of 4 keys:

# for light_mapping_list in list_of_mappings:
#     for i in range(list_of_mappings.index(light_mapping_list)+1, 16):
#         for j in range(list_of_mappings.index(light_mapping_list) + 1, 16):
#             for k in range(list_of_mappings.index(light_mapping_list) + 1, 16):
#                 for pos in light_mapping_list:
#                     lights[pos] = int(not lights[pos])
#                 for second_operand_pos in list_of_mappings[i]:
#                     lights[second_operand_pos] = int(not lights[second_operand_pos])
#                 for third_operand_pos in list_of_mappings[j]:
#                     lights[third_operand_pos] = int(not lights[third_operand_pos])
#                 for fourth_operand_pos in list_of_mappings[k]:
#                     lights[fourth_operand_pos] = int(not lights[fourth_operand_pos])
#                 if lights.count(1) <= 3:
#                     print(f"Lights after {list_of_mappings.index(light_mapping_list) + 1} + {i+1} + {j+1} + {k+1} = {lights}")
#                 lights = [0]*16

# As you can see there is a pattern to this algorithm, so it is easy for you to extend it to higher sums, just be sure
# to have enough computer power :P (most max out at 7)

# ALGORITHM FOR 6 KEYS:   [I absolutely LOVE this algo, it's so OP, like forget getting 2 key flipped cases(not that those aren't good, they're AMAZING but), you can literally solve the whole puzzle by putting in your state]

# for light_mapping_list in list_of_mappings:
#     for i in range(list_of_mappings.index(light_mapping_list)+1, 16):
#         for j in range(list_of_mappings.index(light_mapping_list) + 1, 16):
#             for k in range(list_of_mappings.index(light_mapping_list) + 1, 16):
#                 for l in range(list_of_mappings.index(light_mapping_list) + 1, 16):
#                     for m in range(list_of_mappings.index(light_mapping_list) + 1, 16):
#                             for pos in light_mapping_list:
#                                 lights[pos] = int(not lights[pos])
#                             for second_operand_pos in list_of_mappings[i]:
#                                 lights[second_operand_pos] = int(not lights[second_operand_pos])
#                             for third_operand_pos in list_of_mappings[j]:
#                                 lights[third_operand_pos] = int(not lights[third_operand_pos])
#                             for fourth_operand_pos in list_of_mappings[k]:
#                                 lights[fourth_operand_pos] = int(not lights[fourth_operand_pos])
#                             for fifth_operand_pos in list_of_mappings[l]:
#                                 lights[fifth_operand_pos] = int(not lights[fifth_operand_pos])
#                             for sixth_operand_pos in list_of_mappings[m]:
#                                 lights[sixth_operand_pos] = int(not lights[sixth_operand_pos])
#                             if lights == [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
#                                 print(f"Lights after {list_of_mappings.index(light_mapping_list) + 1} + {i+1} + {j+1} + {k+1} + {l+1} + {m+1} = {lights}")
#                             lights = [0]*16


# Solution for (0,6):
#
# 5 steps: 1 + 2 + 3 + 8 + 16 (found using above algo, 5th variant in 2 sec)
#
# 6 steps: 1 + 3 + 5 + 11 + 14 + 16 (found using above algo in 13 sec)
