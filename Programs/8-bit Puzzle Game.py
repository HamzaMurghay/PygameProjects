import pygame as pg

# Setting up Basic Pygame Pre-requisites -----------------------------------------------------------------------

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("8-bit Puzzle Game")
# pg.display.set_icon()  # Implement this feature later
# pg.display.set_allow_screensaver()  # Implement this feature later
clock = pg.time.Clock()

pg.init()

# Setting up Fonts ---------------------------------------------------------------------------------------------

textbox_font = pg.font.Font("../assets/fonts/garet/Garet-Book.ttf", 16)

namebar_font_big = pg.font.Font("../assets/fonts/garet/Garet-Heavy.ttf", 18)
namebar_font_small = pg.font.Font('../assets/fonts/garet/Garet-Heavy.ttf', 12)


level_description_title_font = pg.font.Font('../assets/fonts/garet/Garet-Heavy.ttf', 34)
level_description_body_font = pg.font.Font('../assets/fonts/garet/Garet-Book.ttf', 24)

# Importing Game Images and other elements ---------------------------------------------------------------------

cave_backg = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/cave background.png').convert_alpha()
cave_backg_faded = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/cave background_faded.png').convert_alpha()
textbox = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/textbox_trimmed.png').convert_alpha()

ee_happy = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/expert_explorer_happy_trimmed.jpg.png').convert_alpha()
ee_shocked1 = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/expert_explorer_shocked_trimmed1.png').convert_alpha()
ee_shocked2 = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/expert_explorer_shocked_trimmed2.png').convert_alpha()
ee_angry = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/expert_explorer_angry_trimmed.png').convert_alpha()

level_select_menu = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/level select menu.png').convert_alpha()
level_description_backg = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/level_description.png')

level_lock_chains = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/chains_trimmed.png').convert_alpha()
level_lock_chains_inverted = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/chains_inv_trimmed.png').convert_alpha()
level_start_button = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/start_button_trimmed.png').convert_alpha()
level_start_button_rect = level_start_button.get_rect(topleft=(233, 360))

back_button = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/back_arrow.png').convert_alpha()
back_button_rect = back_button.get_rect(topleft=(140, 134))

chain_sound = pg.mixer.Sound('../assets/sounds/8-Bit Pixel Game/metal_chain_sound.mp3')

click_cursor = pg.image.load('../assets/graphics/8-Bit Pixel Game/main_code/Pointing_hand_cursor.svg.png').convert_alpha()
change_mouse = False

# Setting up Textbox Text and Related Variables ----------------------------------------------------------------

empty_line = textbox_font.render("", True, 'black')
text_lines = [empty_line]  # This list stores the surfaces of text lines needed in textbox,a for loop will blit them all
current_line_rect = text_lines[0].get_rect(topleft=(5, 500))

namebar_text = namebar_font_big.render("??????", True, 'White')
namebar_text2 = namebar_font_big.render("", True, 'White')  # This is just one line

current_letter_idx = 0
print_is_ongoing = True
running_text = " "
lines_done = 0
caret_position = 0

# Defining Textbox Related Functions ---------------------------------------------------------------------------


def write_in_textbox(string: str):  # This function writes in the area of the textbox in typewriter style
    global current_letter_idx, text_lines, running_text, lines_done, caret_position, current_line_rect, print_is_ongoing

    if current_letter_idx < len(string) and print_is_ongoing:

        caret_position = current_line_rect.right

        if caret_position > 485 and running_text[len(running_text) - 1] == ' ':
            lines_done += 1
            running_text = " "
            running_text += string[current_letter_idx]
            text_lines.append((textbox_font.render(running_text, True, (123, 220, 255))))

        else:
            running_text += string[current_letter_idx]
            text_lines[lines_done] = textbox_font.render(running_text, True, (123, 220, 255))
        current_letter_idx += 1

    elif current_letter_idx == len(string):
        current_letter_idx = 0
        lines_done = 0
        running_text = " "
        print_is_ongoing = False


def go_to_next_dialogue():  # Clears list text_lines and resets variables in order to make way for the new dialogue text
    global text_lines, empty_line, dialogue_index, current_line_rect, print_is_ongoing, current_letter_idx, running_text

    text_lines.clear()
    text_lines.append(empty_line)
    current_line_rect = text_lines[0].get_rect(topleft=(15, 500))

    current_letter_idx = 0
    running_text = " "
    dialogue_index += 1
    print_is_ongoing = True

    return 0


# Defining Sprite "Animation" Function -------------------------------------------------------------------------

switch_sprite_counter = -1
popup_animation_y_value = 370


def chose_ee_sprite():  # Chooses the appropriate ee(expert explorer) sprite to be displayed based on current dialogue
    global dialogue_index, namebar_text, namebar_text2, popup_animation_y_value, switch_sprite_counter

    reached_max_height = False

    if dialogue_index == 0:

        if popup_animation_y_value >= 298 and not reached_max_height:
            popup_animation_y_value -= 2
        elif popup_animation_y_value <= 300 and reached_max_height:
            popup_animation_y_value += 2
        else:
            reached_max_height = True

        return ee_happy, (0, int(popup_animation_y_value))

    elif dialogue_index == 1:
        namebar_text = namebar_font_small.render("Best Explorer", True, 'White')
        namebar_text2 = namebar_font_small.render("(Apparently)", True, 'White')

        if switch_sprite_counter < 52: switch_sprite_counter += 1  # These two lines facilitate the shocked animation
        return (ee_shocked2, (-35, 280)) if switch_sprite_counter % 10 == 0 else (ee_shocked1, (-35, 280))

    else:
        return ee_angry, (50, 270)


# Defining Level Menu Related Functions ------------------------------------------------------------------------


def show_level_status(level):
    global current_letter_idx, lines_done, running_text, current_line_rect, text_lines

    if not level: return

    if level <= (levels_completed + 1):  # If the level whose status is asked is not locked
        for render_text, render_coords in level_descriptions[level - 1]: screen.blit(render_text, render_coords)

    else:
        if (pg.time.get_ticks() - time_since_clicked) < 10: go_to_next_dialogue()  # This ensures that repeatedly clicking different locked levels doesn't glitch out the textbox

        write_in_textbox("This level is locked, complete the previous levels to unlock it.")
        screen.blit(text_lines[0], (current_line_rect.topleft[0] + 30, current_line_rect.topleft[1]))


def display_level_description_background():
    screen.fill('#1c1730')
    screen.blit(cave_backg_faded, (0, 0))
    pg.draw.rect(screen, "Black", pg.Rect(106, 71, 383, 383), 8, 2)

    screen.blit(level_description_backg, (110, 75))
    screen.blit(back_button, back_button_rect)
    screen.blit(level_start_button, level_start_button_rect)


# Setting Up Pre-Defined Dialogues And Level Descriptions ------------------------------------------------------

intro_dialogue = ["Heya chump! I see you're new here, if you don't know what's going on, don't worry! You have me! The "
                  "best traveller in the entire continent of FERALIS to help you out, UwU!",

                  "What's that? You don't believe me?? Hmph! You think I'd lie about being the best explorer? Huh! You "
                  "must think you're so great huh, that you think you don't even need me, HMPH!!!",

                  "Alright then! See if you can solve these 5 puzzles on your own without me, I was going to help you "
                  "but not anymore! Dont come crying to me later when you aren't able to solve them!",

                  "It's not like you need to solve these 5 puzzles to get out of this cave or anything....now go! I "
                  "dont want to see you anymore >_<"]

personal_thoughts = ["(Okayyyyy, that was...interesting. Anyway,so let's think: I'm somewhere in a cave, I have no idea"
                     " how I got here, who I am, my name is..? It's Zir..Zira? Zirion...? Something with Zir...)",

                     "(Now besides that, I'm trapped in a cave, with no idea how to get out....but he did say to solve "
                     "5 puzzles or something...let's try that for now.)"]

level_descriptions = (
    (
        (level_description_title_font.render("LEVEL 1", True, 'gold'), (232, 173)),
        (level_description_body_font.render("Objectives -", True, "white"), (150, 255)),
        (level_description_body_font.render("> Explore the cave to find", True, "white"), (150, 295)),
        (level_description_body_font.render("any usable resources.", True, "white"), (171, 315))
    ),
)

# Main Loop Variable Declarations ------------------------------------------------------------------------------

dialogue_index = 0
intro_done = personal_thoughts_done = False

show_level_select_menu = False
show_specific_level_description = False

levels_completed = 0

# This list has the coordinates of where the chains for locked levels need to be placed
locked_levels_chains = [[(260, 256), (248, 260)], [(375, 256), (365, 260)],
                        [(200, 350), (189, 353)], [(318, 350), (306, 353)]]

# These are the hit boxes for the levels that transform your cursor when you hover over it and detect when you click it
l1_circle = pg.draw.circle(screen, "black", (187, 293), 41)
l2_circle = pg.draw.circle(screen, "black", (292, 293), 42)
l3_circle = pg.draw.circle(screen, "black", (410, 293), 41)
l4_circle = pg.draw.circle(screen, "black", (233, 385), 42)
l5_circle = pg.draw.circle(screen, "black", (350, 385), 42)

cursor_collision = [l1_circle, l2_circle, l3_circle, l4_circle, l5_circle, back_button_rect, level_start_button_rect]  # This list contains the elements to check if the cursor collides with and thus change the cursor to a click cursor along with the boolean values of whether they are on screen or not

give_level_status_of = 0  # Says which level to show status of, 0 if no level was clicked by user in level select menu
time_since_clicked = 0

# Main Loop ----------------------------------------------------------------------------------------------------

while True:
    mouse_pos = pg.mouse.get_pos()

    for event in pg.event.get():  # Checks for any meaningful user event taking place
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if (event.type == pg.KEYUP and event.key == pg.K_SPACE) and running_text == " ":
            if not intro_done:
                if dialogue_index == len(intro_dialogue) - 1:
                    intro_done = True
                    print_is_ongoing = False
                    dialogue_index = -1
                go_to_next_dialogue()

            elif not personal_thoughts_done:
                if dialogue_index == len(personal_thoughts) - 1:
                    personal_thoughts_done = True
                    show_level_select_menu = True
                    print_is_ongoing = False
                    dialogue_index = -1
                go_to_next_dialogue()

        for current_index, collision_obj in enumerate(cursor_collision):

            if show_level_select_menu and collision_obj.collidepoint(mouse_pos) and current_index < 5:
                pg.mouse.set_visible(False)
                change_mouse = True

                if event.type == pg.MOUSEBUTTONUP:
                    give_level_status_of = current_index + 1  # +1 is only for reader to understand which level is being asked for, during execution +1 is nullified

                    if levels_completed >= current_index:
                        show_level_select_menu = False
                        show_specific_level_description = True
                    else:
                        chain_sound.play()
                        time_since_clicked = pg.time.get_ticks()
                break

            elif show_specific_level_description and collision_obj.collidepoint(mouse_pos) and current_index >= 5:
                pg.mouse.set_visible(False)
                change_mouse = True

                if current_index == 5 and event.type == pg.MOUSEBUTTONUP:
                    show_specific_level_description = False
                    show_level_select_menu = True
                    give_level_status_of = 0
                else:
                    pass
                break
        else:
            pg.mouse.set_visible(True)
            change_mouse = False

    screen.fill((71, 59, 123))
    screen.blit(cave_backg, (0, 0))

    if not intro_done:

        write_in_textbox(intro_dialogue[dialogue_index])

        screen.blit(chose_ee_sprite()[0], chose_ee_sprite()[1])
        screen.blit(textbox, (-282, 240))

        if dialogue_index == 0:
            screen.blit(namebar_text, (67, 454))

        else:
            screen.blit(namebar_text, (55, 453))
            screen.blit(namebar_text2, (56, 465))

        for line in text_lines:
            line_in_list = text_lines.index(line)
            current_line_rect = text_lines[line_in_list].get_rect(topleft=(15, (500 + line_in_list * 18)))
            screen.blit(text_lines[text_lines.index(line)], current_line_rect)

    elif not personal_thoughts_done:
        namebar_text = namebar_font_big.render("You", True, 'White')
        write_in_textbox(personal_thoughts[dialogue_index])

        screen.blit(textbox, (-282, 240))
        screen.blit(namebar_text, (78, 454))

        for line in text_lines:
            line_in_list = text_lines.index(line)
            current_line_rect = text_lines[line_in_list].get_rect(topleft=(15, (500 + line_in_list * 18)))
            screen.blit(text_lines[text_lines.index(line)], current_line_rect)

    elif show_level_select_menu:
        screen.fill('#1c1730')
        screen.blit(cave_backg_faded, (0, 0))
        pg.draw.rect(screen, "Black", pg.Rect(106, 71, 383, 383), 8, 2)
        screen.blit(level_select_menu, (110, 75))

        for chain1_coord, chain2_coord in locked_levels_chains:  # Renders the locked level chains on each locked level
            screen.blit(level_lock_chains_inverted, chain1_coord)
            screen.blit(level_lock_chains, chain2_coord)

        show_level_status(give_level_status_of)
        if running_text == " " and pg.time.get_ticks() - time_since_clicked > 2800: give_level_status_of = go_to_next_dialogue()

    elif show_specific_level_description:
        display_level_description_background()
        show_level_status(give_level_status_of)

    if change_mouse: screen.blit(click_cursor, (mouse_pos[0] - 15, mouse_pos[1]))

    pg.display.update()
    clock.tick(60)
