import pygame as pg

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("8-bit Puzzle Game")
clock = pg.time.Clock()

pg.init()

textbox_font = pg.font.Font("fonts/garet/Garet-Book.ttf", 16)
name_font = pg.font.Font("fonts/garet/Garet-Heavy.ttf", 18)

line1 = textbox_font.render("", True, 'black')
text_lines = [line1]
current_line_rect = text_lines[0].get_rect(topleft=(5, 500))

namebar_text = name_font.render("??????", True, 'White')
namebar_text2 = name_font.render("", True, 'White')


letter_index = 0
ongoing_print = True
running_text = " "
lines_done = 0
caret_position = 0


def write_in_textbox(string: str):
    global letter_index, text_lines, running_text, lines_done, caret_position, current_line_rect, ongoing_print

    if letter_index < len(string) and ongoing_print:

        ongoing_print = True
        caret_position = current_line_rect.right

        if caret_position > 485 and running_text[len(running_text) - 1] == ' ':
            lines_done += 1
            running_text = " "
            running_text += string[letter_index]
            text_lines.append((textbox_font.render(running_text, True, (123, 220, 255))))

        else:
            running_text += string[letter_index]
            text_lines[lines_done] = textbox_font.render(running_text, True, (123, 220, 255))
        letter_index += 1

    elif letter_index == len(string):
        letter_index = 0
        lines_done = 0
        running_text = " "
        ongoing_print = False


def go_to_next_line():

    global text_lines, line1, dialouge_index, current_line_rect, ongoing_print, lines_done
    text_lines.clear()
    text_lines.append(line1)
    dialouge_index += 1
    current_line_rect = text_lines[lines_done].get_rect(topleft=(15, 500))
    ongoing_print = True


cave_backg = pg.image.load('graphics/8-Bit Pixel Game/cave background.png').convert_alpha()
cave_backg_faded = pg.image.load('graphics/8-Bit Pixel Game/cave background_faded.png').convert_alpha()
textbox = pg.image.load('graphics/8-Bit Pixel Game/textbox_trimmed.png').convert_alpha()

ee_happy = pg.image.load('graphics/8-Bit Pixel Game/expert_explorer_happy_trimmed.jpg.png').convert_alpha()
ee_shocked1 = pg.image.load('graphics/8-Bit Pixel Game/expert_explorer_shocked_trimmed1.png').convert_alpha()
ee_shocked2 = pg.image.load('graphics/8-Bit Pixel Game/expert_explorer_shocked_trimmed2.png').convert_alpha()
ee_angry = pg.image.load('graphics/8-Bit Pixel Game/expert_explorer_angry_trimmed.png').convert_alpha()

level_select_menu = pg.image.load('graphics/8-Bit Pixel Game/level select menu.png').convert_alpha()
lock_chains = pg.image.load('graphics/8-Bit Pixel Game/chains_trimmed.png').convert_alpha()
lock_chains_inverted = pg.image.load('graphics/8-Bit Pixel Game/chains_inverted_trimmed.png').convert_alpha()

chain_sound = pg.mixer.Sound('sounds/8-Bit Pixel Game/metal_chain_sound.mp3')

click_cursor = pg.image.load('graphics/8-Bit Pixel Game/Pointing_hand_cursor.svg.png').convert_alpha()
change_mouse = False

iterate = -1
popup_animation_iter = 370
reached_max_height = False


def chose_ee_sprite():
    global dialouge_index, iterate, namebar_text, namebar_text2, popup_animation_iter, reached_max_height

    if dialouge_index == 0:

        if popup_animation_iter >= 298 and not reached_max_height:
            popup_animation_iter -= 2
        elif popup_animation_iter <= 300 and reached_max_height:
            popup_animation_iter += 2
        else:
            reached_max_height = True

        return ee_happy, (0, int(popup_animation_iter))

    if dialouge_index == 1:
        namebar_font = pg.font.Font('fonts/garet/Garet-Heavy.ttf', 12)
        namebar_text = namebar_font.render("Best Explorer", True, 'White')
        namebar_text2 = namebar_font.render("(Apparently)", True, 'White')

        iterate += 1

        if iterate % 10 == 0 and iterate < 51:
            return ee_shocked2, (-35, 280)
        else:
            return ee_shocked1, (-35, 280)

    if dialouge_index == 2 or dialouge_index == 3:
        return ee_angry, (50, 270)


intro_dialouge = ["Heya chump! I see you're new here, if you don't know what's going on, don't worry! You have me! The "
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

dialouge_index = 0
intro_done = False
personal_thoughts_done = False
level1_done, level1_locked = False, False
level2_done, level2_locked = False, True
level3_done, level3_locked = False, True
level4_done, level4_locked = False, True
level5_done, level5_locked = False, True

l1_circle = pg.draw.circle(screen, "black", (187, 293), 41)
l2_circle = pg.draw.circle(screen, "black", (292, 293), 42)
l3_circle = pg.draw.circle(screen, "black", (410, 293), 41)
l4_circle = pg.draw.circle(screen, "black", (233, 385), 42)
l5_circle = pg.draw.circle(screen, "black", (350, 385), 42)

give_level1_status = False
give_level2_status = False
give_level3_status = False
give_level4_status = False
give_level5_status = False

level_statuses = [True, "This level is locked, complete the previous levels to unlock it."]

level1_status = level_statuses[0]
level2_status = level_statuses[1]
level3_status = level_statuses[1]
level4_status = level_statuses[1]
level5_status = level_statuses[1]


def show_level_status(current_level_status):
    global letter_index, lines_done, running_text, current_line_rect, text_lines

    if pg.time.get_ticks() - time_since_clicked < 10:
        letter_index = 0
        lines_done = 0
        running_text = " "
        go_to_next_line()

    write_in_textbox(current_level_status)
    screen.blit(text_lines[0], (current_line_rect.topleft[0] + 30, current_line_rect.topleft[1]))


time_since_clicked = 0
while True:
    mouse = pg.mouse

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYUP and event.key == pg.K_SPACE and running_text == " ":
            if not intro_done:
                if dialouge_index != len(intro_dialouge) - 1:
                    go_to_next_line()
                else:
                    intro_done = True
                    ongoing_print = False
                    dialouge_index = -1
                    go_to_next_line()

            elif not personal_thoughts_done:
                if dialouge_index != len(personal_thoughts) - 1:
                    go_to_next_line()
                else:
                    personal_thoughts_done = True
                    ongoing_print = False
                    dialouge_index = -1
                    go_to_next_line()

        if (l1_circle.collidepoint(mouse.get_pos()) or l2_circle.collidepoint(mouse.get_pos())
            or l3_circle.collidepoint(mouse.get_pos()) or l4_circle.collidepoint(mouse.get_pos())
                or l5_circle.collidepoint(mouse.get_pos())) and personal_thoughts_done:

            mouse.set_visible(False)
            change_mouse = True
            if event.type == pg.MOUSEBUTTONUP and l1_circle.collidepoint(mouse.get_pos()):
                give_level1_status = True
            if event.type == pg.MOUSEBUTTONUP and l2_circle.collidepoint(mouse.get_pos()):
                give_level2_status = True
                if level2_locked:
                    chain_sound.play()
                    time_since_clicked = pg.time.get_ticks()
            if event.type == pg.MOUSEBUTTONUP and l3_circle.collidepoint(mouse.get_pos()):
                give_level3_status = True
                if level3_locked:
                    chain_sound.play()
                    time_since_clicked = pg.time.get_ticks()

            if event.type == pg.MOUSEBUTTONUP and l4_circle.collidepoint(mouse.get_pos()):
                give_level4_status = True
                if level4_locked:
                    chain_sound.play()
                    time_since_clicked = pg.time.get_ticks()
            if event.type == pg.MOUSEBUTTONUP and l5_circle.collidepoint(mouse.get_pos()):
                give_level5_status = True
                if level5_locked:
                    chain_sound.play()
                    time_since_clicked = pg.time.get_ticks()

        else:
            mouse.set_visible(True)
            change_mouse = False

    screen.fill((71, 59, 123))
    screen.blit(cave_backg, (0, 0))

    if not intro_done:

        write_in_textbox(intro_dialouge[dialouge_index])

        screen.blit(chose_ee_sprite()[0], chose_ee_sprite()[1])
        screen.blit(textbox, (-282, 240))

        if dialouge_index == 0:
            screen.blit(namebar_text, (67, 454))

        else:
            screen.blit(namebar_text, (55, 453))
            screen.blit(namebar_text2, (56, 465))

        for line in text_lines:
            line_in_listno = text_lines.index(line)
            current_line_rect = text_lines[line_in_listno].get_rect(topleft=(15, (500 + line_in_listno * 18)))
            screen.blit(text_lines[text_lines.index(line)], current_line_rect)

    elif intro_done and not personal_thoughts_done:
        namebar_text = name_font.render("You", True, 'White')
        write_in_textbox(personal_thoughts[dialouge_index])

        screen.blit(textbox, (-282, 240))
        screen.blit(namebar_text, (78, 454))

        for line in text_lines:
            line_in_listno = text_lines.index(line)
            current_line_rect = text_lines[line_in_listno].get_rect(topleft=(15, (500 + line_in_listno * 18)))
            screen.blit(text_lines[text_lines.index(line)], current_line_rect)

    elif personal_thoughts_done:
        screen.fill('#1c1730')
        screen.blit(cave_backg_faded, (0, 0))
        pg.draw.rect(screen, "Black", pg.Rect(106, 71, 383, 383), 8, 2)
        screen.blit(level_select_menu, (110, 75))

        if level2_locked:
            screen.blit(lock_chains_inverted, (260, 256))
            screen.blit(lock_chains, (248, 260))
            if give_level2_status:
                give_level1_status, give_level3_status, give_level4_status, give_level5_status = False, False, False, \
                                                                                                 False
                show_level_status(level2_status)
                if running_text == " " and pg.time.get_ticks() - time_since_clicked > 2800:
                    go_to_next_line()
                    give_level2_status = False

        if level3_locked:
            screen.blit(lock_chains_inverted, (375, 256))
            screen.blit(lock_chains, (365, 260))
            if give_level3_status:
                give_level1_status, give_level2_status, give_level4_status, give_level5_status = False, False, False, \
                                                                                                 False
                show_level_status(level3_status)
                if running_text == " " and pg.time.get_ticks() - time_since_clicked > 2800:
                    go_to_next_line()
                    give_level3_status = False

        if level4_locked:
            screen.blit(lock_chains_inverted, (200, 350))
            screen.blit(lock_chains, (189, 353))
            if give_level4_status:
                give_level1_status, give_level2_status, give_level3_status, give_level5_status = False, False, False, \
                                                                                                 False
                show_level_status(level4_status)
                if running_text == " " and pg.time.get_ticks() - time_since_clicked > 2800:
                    go_to_next_line()
                    give_level4_status = False

        if level5_locked:
            screen.blit(lock_chains_inverted, (318, 350))
            screen.blit(lock_chains, (306, 353))
            if give_level5_status:
                give_level1_status, give_level2_status, give_level3_status, give_level4_status = False, False, False, \
                                                                                                 False
                show_level_status(level5_status)
                if running_text == " " and pg.time.get_ticks() - time_since_clicked > 2800:
                    go_to_next_line()
                    give_level5_status = False

    if change_mouse:
        screen.blit(click_cursor, (mouse.get_pos()[0]-15, mouse.get_pos()[1]))

    pg.display.update()
    clock.tick(60)

# Pro-tip: be careful when copying and pasting code, you may by mistake copy that function with the wrong parameters
# and then forget to change them, this happened to me in rps program and was a huge reason why my avoiding algorithm
# wasn't working at the start, so note: if the program isn't working how it's supposed to, but there are no errors or
# any other code function that's wrong, check the arguments put in
