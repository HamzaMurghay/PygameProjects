import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((600, 600))
pg.display.set_caption('Rock Paper Scissors Simulator')
clock = pg.time.Clock()
text_font = pg.font.Font('fonts/primeform_pro/PrimeformProDemo-Light.otf', 20)
text_smallerfont = pg.font.Font('fonts/primeform_pro/PrimeformProDemo-Light.otf', 13)


class Rock:
    rock_surface = pg.image.load('graphics/rockT.png').convert_alpha()
    speed_x = speed_y = 1
    direction_x = direction_y = 1


class Paper:
    paper_surface = pg.image.load('graphics/paperT.png').convert_alpha()
    rectangle = None
    speed_x = speed_y = 1
    direction_x = direction_y = 1


class Scissor:
    scissor_surface = pg.image.load('graphics/scissorsT.png').convert_alpha()
    rectangle = None
    speed_x = speed_y = 1
    direction_x = direction_y = 1


def create_all_objects():
    rocks_list = [Rock() for i in range(33)]

    papers_list = [Paper() for i in range(33)]

    scissors_list = [Scissor() for i in range(33)]

    return rocks_list, papers_list, scissors_list


def collision_during_placement(object_being_placed, object_already_there_list):
    for entity in object_already_there_list:
        if object_being_placed.rectangle.colliderect(entity.rectangle):
            return True
    return False


def place_all_objects():
    for rock in rock_list:
        rock.rectangle = rock.rock_surface.get_rect(topleft=(random.randint(4, 577), random.randint(82, 575)))
        # Creating rock rectangle object

    for paper in paper_list:
        paper.rectangle = paper.paper_surface.get_rect(topleft=(random.randint(4, 577), random.randint(82, 572)))
        while collision_during_placement(paper, rock_list):
            paper.rectangle = paper.paper_surface.get_rect(topleft=(random.randint(4, 577), random.randint(82, 572)))

    for scissor in scissor_list:
        scissor.rectangle = scissor.scissor_surface.get_rect(topleft=(random.randint(4, 565), random.randint(82, 572)))
        while collision_during_placement(scissor, rock_list) or collision_during_placement(scissor, paper_list):
            scissor.rectangle = scissor.scissor_surface.get_rect(
                topleft=(random.randint(4, 565), random.randint(82, 572)))


pauseb_surface = pg.image.load('graphics/pausebutton.jpg').convert_alpha()
pause_button_rectangle = pauseb_surface.get_rect(topleft=(16, 7))

current_play_state_surface = playb_surface = pg.image.load('graphics/playbutton.jpg').convert_alpha()  # we define two variables , play_button and its surface and rectangle, along with current_play_state and its surface and rectangle, play button contains the play button surface image and its rectangle. it is constant, however  current_play_state will keep alternating and changing between being equal to the play button and the pause button, but at the start, we define it as equal to the play button, which will change later on
current_play_state_rectangle = play_button_rectangle = playb_surface.get_rect(topleft=(15, 7))

resetb_surface = pg.image.load('graphics/reset button.png').convert_alpha()
reset_button_rectangle = resetb_surface.get_rect(topleft=(17, 45))

fast_forward_button_surface = pg.image.load('graphics/fastForwardsmall.png')
fast_forward_button_rectangle = fast_forward_button_surface.get_rect(topleft=(525, 45))

avoid_algo_toggle_ON = pg.image.load('graphics/ToggleON.png')
avoid_algo_toggle_transition1 = pg.image.load('graphics/ToggleTransition1.png')
avoid_algo_toggle_transition2 = pg.image.load('graphics/ToggleTransition2.png')
avoid_algo_toggle_OFF = pg.image.load('graphics/ToggleOFF.png')

avoid_algo_toggle_transition_states = [avoid_algo_toggle_ON, avoid_algo_toggle_transition1,
                                       avoid_algo_toggle_transition2, avoid_algo_toggle_OFF]
transition_index = 0

avoid_algo_toggle_surface = avoid_algo_toggle_transition_states[transition_index]
avoid_algo_toggle_rectangle = avoid_algo_toggle_surface.get_rect(topleft=(545, 13))


def adjust_toggle_rectangle_position():
    if int(transition_index) == 0:
        avoid_algo_toggle_rectangle.topleft = (545, 13)
    elif int(transition_index) == 1:
        avoid_algo_toggle_rectangle.topleft = (547, 15)
    elif int(transition_index) == 2:
        avoid_algo_toggle_rectangle.topleft = (547, 15)
    elif int(transition_index) == 3:
        avoid_algo_toggle_rectangle.topleft = (548, 16)


do_play = 0

rock_num, paper_num, scissor_num = 33, 33, 33

rock_list, paper_list, scissor_list = create_all_objects()
place_all_objects()

winner = None

rock_win_num, paper_win_num, scissor_win_num = 0, 0, 0  # denotes number of wins for each class

tick_rate = 60

fast_forward = False

keep_avoiding_algo_on = 1

current_time = 0
toggle_press_time = 0
toggle_state = False


def draw_text_and_borders():
    rocks_num_surface = text_font.render(f'Rocks - {rock_num}', True, 'black')
    rocks_num_rectangle = rocks_num_surface.get_rect(topleft=(81, 20))

    paper_num_surface = text_font.render(f'Papers - {paper_num}', True, 'black')
    paper_num_rectangle = paper_num_surface.get_rect(topleft=(208, 20))

    scissors_num_surface = text_font.render(f'Scissors - {scissor_num}', True, 'black')
    scissors_num_rectangle = scissors_num_surface.get_rect(topleft=(338, 20))

    avoid_algo_surface1 = text_smallerfont.render('Avoid', True, 'Black')
    avoid_algo_rectangle1 = avoid_algo_surface1.get_rect(topleft=(494, 15))

    avoid_algo_surface2 = text_smallerfont.render('Enemies', True, 'Black')
    avoid_algo_rectangle2 = avoid_algo_surface2.get_rect(topleft=(485, 27))

    pg.draw.rect(screen, 'Gray', pg.Rect(75, 18, 114, 28), 2,
                 10)  # pg.Rect(startposition_x, startposition_y, size_of_rect_x, size_of_rect_y)
    screen.blit(rocks_num_surface, rocks_num_rectangle)

    pg.draw.rect(screen, 'Red', pg.Rect(202, 18, 122, 28), 2, 10)
    screen.blit(paper_num_surface, paper_num_rectangle)

    pg.draw.rect(screen, 'Blue', pg.Rect(332, 18, 133, 28), 2, 10)
    screen.blit(scissors_num_surface, scissors_num_rectangle)

    screen.blit(avoid_algo_surface1, avoid_algo_rectangle1)

    screen.blit(avoid_algo_surface2, avoid_algo_rectangle2)

    # -----------------------------------------------------------------------------------------------

    rock_win_num_surface = text_font.render(f'Wins - {rock_win_num}', True, 'black')
    rock_win_num_rectangle = rocks_num_surface.get_rect(topleft=(95, 50))

    paper_win_num_surface = text_font.render(f'Wins - {paper_win_num}', True, 'black')
    paper_win_num_rectangle = rocks_num_surface.get_rect(topleft=(225, 50))

    scissor_win_num_surface = text_font.render(f'Wins - {scissor_win_num}', True, 'black')
    scissor_win_num_rectangle = rocks_num_surface.get_rect(topleft=(360, 50))

    screen.blit(rock_win_num_surface, rock_win_num_rectangle)
    screen.blit(paper_win_num_surface, paper_win_num_rectangle)
    screen.blit(scissor_win_num_surface, scissor_win_num_rectangle)


def chase_closest_defeatable_enemy(chaser, chased_list, chased_num):
    if chased_num > 0:
        chaser_and_chased_distances = []
        chased_entities_of_particular_distance = []

        chaser_x = chaser.rectangle.centerx
        chaser_y = chaser.rectangle.centery

        for chased in chased_list:
            chased_x = chased.rectangle.centerx
            chased_y = chased.rectangle.centery

            distance_away = ((chaser_x - chased_x) ** 2 + (chaser_y - chased_y) ** 2)
            chaser_and_chased_distances.append(distance_away)
            chased_entities_of_particular_distance.append(chased)
        closest_chased_entity = chased_entities_of_particular_distance[
            chaser_and_chased_distances.index(min(chaser_and_chased_distances))]

        if abs(chaser.rectangle.left + chaser.speed_x - closest_chased_entity.rectangle.left) < abs(
                chaser.rectangle.left - chaser.speed_x - closest_chased_entity.rectangle.left):
            chaser.rectangle.left += chaser.speed_x * chaser.direction_x
        else:
            chaser.rectangle.left -= chaser.speed_x * chaser.direction_x
        if abs(chaser.rectangle.top + chaser.speed_y - closest_chased_entity.rectangle.top) < abs(
                chaser.rectangle.top - chaser.speed_y - closest_chased_entity.rectangle.top):
            chaser.rectangle.top += chaser.speed_y * chaser.direction_y
        else:
            chaser.rectangle.top -= chaser.speed_y * chaser.direction_y


def avoid_closest_undefeatable_enemy(avoider, obj_avoided_list, obj_avoided_num):
    if obj_avoided_num > 0:
        avoider_obj_avoided_distances, objs_avoided_of_particular_distance = [], []
        avoider_x = avoider.rectangle.centerx
        avoider_y = avoider.rectangle.centery

        for obj_avoided in obj_avoided_list:
            obj_avoided_x = obj_avoided.rectangle.centerx
            obj_avoided_y = obj_avoided.rectangle.centery

            distance_away = ((avoider_x - obj_avoided_x) ** 2 + (avoider_y - obj_avoided_y) ** 2)
            avoider_obj_avoided_distances.append(distance_away)
            objs_avoided_of_particular_distance.append(obj_avoided)
        closest_obj_to_avoid_entity = objs_avoided_of_particular_distance[
            avoider_obj_avoided_distances.index(min(avoider_obj_avoided_distances))]

        if min(avoider_obj_avoided_distances) <= 2500 and not bounce_if_touch_border(avoider):
            if abs(avoider.rectangle.left + avoider.speed_x - closest_obj_to_avoid_entity.rectangle.left) > abs(
                    avoider.rectangle.left - avoider.speed_x - closest_obj_to_avoid_entity.rectangle.left):
                avoider.rectangle.left += avoider.speed_x * avoider.direction_x
            else:
                avoider.rectangle.left -= avoider.speed_x * avoider.direction_x

            if abs(avoider.rectangle.top + avoider.speed_x - closest_obj_to_avoid_entity.rectangle.top) > abs(
                    avoider.rectangle.top - avoider.speed_x - closest_obj_to_avoid_entity.rectangle.top):
                avoider.rectangle.top += avoider.speed_y * avoider.direction_y
            else:
                avoider.rectangle.top -= avoider.speed_y * avoider.direction_y


def bounce_if_touch_border(obj):
    if obj.rectangle.left <= 2:
        obj.rectangle.left = 2
        obj.direction_x *= -1
        obj.rectangle.left += obj.speed_x
        obj.direction_y *= -1
        return True

    elif obj.rectangle.right >= 598:
        obj.rectangle.right = 598
        obj.direction_x *= -1
        obj.rectangle.right -= obj.speed_x
        obj.direction_x *= -1
        return True

    elif obj.rectangle.top <= 79:
        obj.rectangle.top = 79
        obj.direction_y *= -1
        obj.rectangle.top += obj.speed_y
        obj.direction_y *= -1
        return True

    elif obj.rectangle.bottom >= 600:
        obj.rectangle.bottom = 600
        obj.direction_y *= -1
        obj.rectangle.bottom -= obj.speed_y
        obj.direction_y *= -1
        return True

    else:
        return False


while True:
    mouse = pg.mouse
    current_time = pg.time.get_ticks()

    if rock_num == 99 and do_play == 1:
        rock_win_num += 1
        winner = rock_list
        do_play = 0

    if paper_num == 99 and do_play == 1:
        paper_win_num += 1
        winner = paper_list
        do_play = 0

    if scissor_num == 99 and do_play == 1:
        scissor_win_num += 1
        winner = scissor_list
        do_play = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if (event.type == pg.MOUSEBUTTONUP and current_play_state_rectangle.collidepoint(mouse.get_pos())) or (
                event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
            if current_play_state_surface is playb_surface:
                if not (rock_num == 99 or paper_num == 99 or scissor_num == 99): do_play = 1
                current_play_state_surface = pauseb_surface
                current_play_state_rectangle = pause_button_rectangle
            else:
                do_play = 0
                current_play_state_surface = playb_surface
                current_play_state_rectangle = play_button_rectangle

        if (event.type == pg.MOUSEBUTTONUP and reset_button_rectangle.collidepoint(mouse.get_pos())) or (
                event.type == pg.KEYDOWN and event.key == pg.K_r):
            if winner is None:
                pass
            else:
                winner.clear()

            rock_list, paper_list, scissor_list = create_all_objects()

            place_all_objects()

            if current_play_state_surface is pauseb_surface:
                do_play = 1
            else:
                do_play = 0

        if (event.type == pg.MOUSEBUTTONUP and avoid_algo_toggle_rectangle.collidepoint(mouse.get_pos())) or (event.type == pg.KEYDOWN and event.key == pg.K_t):
            toggle_press_time = pg.time.get_ticks()
            toggle_state = True

        if event.type == pg.KEYDOWN and event.key == pg.K_f or (event.type == pg.MOUSEBUTTONDOWN and fast_forward_button_rectangle.collidepoint(mouse.get_pos())):
            fast_forward = True
        if event.type == pg.KEYUP and event.key == pg.K_f or (event.type == pg.MOUSEBUTTONUP and fast_forward_button_rectangle.collidepoint(mouse.get_pos())):
            fast_forward = False

    screen.fill('white')

    screen.blit(current_play_state_surface, current_play_state_rectangle)
    screen.blit(resetb_surface, reset_button_rectangle)

    if current_time - toggle_press_time < 1000 and toggle_state:
        if keep_avoiding_algo_on:

            if transition_index <= 3.3:
                avoid_algo_toggle_surface = avoid_algo_toggle_transition_states[int(transition_index)]
                adjust_toggle_rectangle_position()
                transition_index += 0.3
            else:
                keep_avoiding_algo_on = 0
                toggle_state = False

        else:

            if transition_index >= 0:
                avoid_algo_toggle_surface = avoid_algo_toggle_transition_states[int(transition_index)]
                adjust_toggle_rectangle_position()
                transition_index -= 0.3
            else:
                keep_avoiding_algo_on = 1
                transition_index = 0
                toggle_state = False

    screen.blit(avoid_algo_toggle_surface, avoid_algo_toggle_rectangle)
    screen.blit(fast_forward_button_surface, fast_forward_button_rectangle)

    draw_text_and_borders()

    game_border = pg.draw.rect(screen, 'Black', pg.Rect(0, 80, 600, 520), 2)
    # Draws black border which represents maximum limit for object travel

    for scissor in scissor_list:
        screen.blit(scissor.scissor_surface, scissor.rectangle)
        # on_collision_change_class(scissor, scissor_list, Scissor(), paper_list)
        for paper in paper_list:  # from here
            if scissor.rectangle.colliderect(paper.rectangle):
                position_temporary = paper.rectangle.topleft
                paper_list.remove(paper)
                paper = Scissor()
                paper.rectangle = paper.scissor_surface.get_rect(topleft=position_temporary)
                scissor_list.append(
                    paper)  # to here is code in order to change the class of a paper when it touches a scissor, similar code is there in every loop for each object when it touches its opponent that it can defeat
                # pg.time.delay(2)
            paper_num = len(paper_list)

        if do_play == 1:

            if keep_avoiding_algo_on:
                avoid_closest_undefeatable_enemy(scissor, rock_list, rock_num)
            chase_closest_defeatable_enemy(scissor, paper_list, paper_num)

        # bounce_if_touch_border(scissor)

    for rock in rock_list:
        screen.blit(rock.rock_surface, rock.rectangle)
        for scissor in scissor_list:

            if rock.rectangle.colliderect(scissor.rectangle):
                position_temporary = scissor.rectangle.topleft
                scissor_list.remove(scissor)
                scissor = Rock()
                scissor.rectangle = scissor.rock_surface.get_rect(topleft=position_temporary)
                rock_list.append(scissor)
                # pg.time.delay(2)
            scissor_num = len(scissor_list)

        if do_play == 1:

            if keep_avoiding_algo_on:
                avoid_closest_undefeatable_enemy(rock, paper_list, paper_num)
            chase_closest_defeatable_enemy(rock, scissor_list, scissor_num)

        # bounce_if_touch_border(rock)

    for paper in paper_list:
        screen.blit(paper.paper_surface, paper.rectangle)
        for rock in rock_list:
            if paper.rectangle.colliderect(rock.rectangle):
                position_temporary = rock.rectangle.topleft
                rock_list.remove(rock)
                rock = Paper()
                rock.rectangle = rock.paper_surface.get_rect(topleft=position_temporary)
                paper_list.append(rock)
                # pg.time.delay(2)
            rock_num = len(rock_list)

        if do_play == 1:
            if keep_avoiding_algo_on:
                avoid_closest_undefeatable_enemy(paper, scissor_list, scissor_num)
            chase_closest_defeatable_enemy(paper, rock_list, rock_num)

        # bounce_if_touch_border(paper)

    rock_num, paper_num, scissor_num = len(rock_list), len(paper_list), len(scissor_list)

    if fast_forward:
        tick_rate = 120
    else:
        tick_rate = 60

    pg.display.update()
    clock.tick(tick_rate)

# def on_collision_change_class(chaser, chaser_list, chaser_class,chased_list):  # This is there to show an idea that I had to reduce the code but the implementation didn't work for some reason that I haven't figured out yet, if I figure it out this will be implemented and this comment removed
#     for chased in chased_list:
#         if chaser.rectangle.colliderect(chased.rectangle):
#             position_temporary = chased.rectangle.topleft
#             chased_list.remove(chased)
#             chased = chaser_class
#             chased.rectangle = chased.surface.get_rect(topleft = position_temporary)
#             chaser_list.append(chased)
#             pg.time.delay(2)
