import pygame as pg

pg.init()


screen = pg.display.set_mode((1920,1080))
clock = pg.time.Clock()


s_x = 350
s_y = 300

rectTL = pg.math.Vector2(765, 350)
rectTR = pg.math.Vector2(765 + s_x, 350)
rectBL = pg.math.Vector2(765, 350 + s_y)
rectBR = pg.math.Vector2(765 + s_x, 350 + s_y)


scrTL = pg.math.Vector2(0,0)
scrTR = pg.math.Vector2(1920,0)
scrBL = pg.math.Vector2(0,1080)
scrBR = pg.math.Vector2(1920,1080)

speed = 1

mouse_dx = mouse_dy = 0

pg.mouse.set_visible(False)
pg.event.set_grab(True)



def borders():

    pg.draw.line(screen, 'black', rectTL, rectTR, 2)
    pg.draw.line(screen, 'black', rectTL, rectBL, 2)
    pg.draw.line(screen, 'black', rectTR, rectBR, 2)
    pg.draw.line(screen, 'black', rectBL, rectBR, 2)


    pg.draw.line(screen, 'black', rectTL, scrTL, 2)
    pg.draw.line(screen, 'black', rectTR, scrTR, 2)
    pg.draw.line(screen, 'black', rectBL, scrBL, 2)
    pg.draw.line(screen, 'black', rectBR, scrBR,2)

def door():

    doorBL = rectBR + (rectBR - scrBR) * 1/5 * rectBR.angle_to(scrBR)
    door_left_frame = doorBL - pg.math.Vector2(0, 300)


    doorBR = rectBR + (rectBR - scrBR) * 2/5 * rectBR.angle_to(scrBR)
    door_right_frame = doorBR - pg.math.Vector2(0, 360) # 300 + 1/5 * 300

    pg.draw.line(screen, 'black', doorBL, door_left_frame, 2)
    pg.draw.line(screen, 'black', doorBR, door_right_frame, 2)
    pg.draw.line(screen, 'black', door_left_frame, door_right_frame, 2)

    pg.draw.circle(screen, 'black', (door_left_frame[0] + 1/64 * door_left_frame[0], door_left_frame[1] + 3/8 * door_left_frame[1]), 7)


while True:
    move = False

    screen.fill((100,100,100))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEMOTION:
            # mouse_dx, mouse_dy = event.rel
            mouse_movement = pg.math.Vector2(event.rel)
            move = True




    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        s_x += speed
        s_y += speed


    elif keys[pg.K_s]:
        s_x -= speed
        s_y -= speed


    if move:
        rectTL[0] += mouse_movement[0]
        rectTR[0] += mouse_movement[0]
        rectBL[0] += mouse_movement[0]
        rectBR[0] += mouse_movement[0]


    # pg.draw.rect(screen, 'black', recta, 2)
    borders()
    door()



    pg.display.update()
    clock.tick(60)



































# import pygame as pg
#
# pg.init()
#
#
# screen = pg.display.set_mode((1920,1080))
# clock = pg.time.Clock()
#
#
# s_x = 100
# s_y = 100
#
# recta = pg.Rect(440,250, s_x,s_y)
# recta2 = pg.Rect(440,250, s_x,s_y)
#
# recta.center = (940, 540)
# recta2.center = (970, 510)
#
# speed = 1
#
# mouse_dx = mouse_dy = 0
#
# pg.mouse.set_visible(False)
# pg.event.set_grab(True)
#
# while True:
#     move = False
#
#     screen.fill((100,100,100))
#
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()
#         if event.type == pg.MOUSEMOTION:
#             mouse_dx, mouse_dy = event.rel
#             move = True
#
#
#     # print(recta.topleft)
#     # print(recta2.topleft)
#
#     keys = pg.key.get_pressed()
#
#     if keys[pg.K_w]:
#         s_x += speed
#         s_y += speed
#         recta.size = (s_x, s_y)
#         # recta.center = (940, recta.center[1] + speed)
#
#         recta2.size = (s_x, s_y)
#     elif keys[pg.K_s]:
#         s_x -= speed
#         s_y -= speed
#         recta.size = (s_x, s_y)
#         # recta.center = (940, recta.center[1] - speed)
#
#         recta2.size = (s_x, s_y)
#
#     # if move:
#     #     recta.center = (recta.center[0] + mouse_dx, recta.center[1])
#
#
#     pg.draw.rect(screen, 'black', recta, 1)
#     pg.draw.rect(screen, 'black', recta2, 1)
#
#     pg.draw.line(screen, 'black',recta.topleft, recta2.topleft)
#     pg.draw.line(screen, 'black',recta.topright, recta2.topright)
#     pg.draw.line(screen, 'black',recta.bottomright, recta2.bottomright)
#     pg.draw.line(screen, 'black',recta.bottomleft, recta2.bottomleft)
#
#     pg.draw.line(screen, 'black', (0, 590), (1920, 590))
#
#
#     pg.display.update()
#     clock.tick(60)