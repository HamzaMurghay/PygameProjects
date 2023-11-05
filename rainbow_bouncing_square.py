import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
screen.fill('white')
pg.display.set_caption('Rainbow Bouncing Square')


b_square_surface = pg.Surface((30, 30))
b_square_rectangle = b_square_surface.get_rect(topleft=(0, 0))

b_square_speedx = 3
b_square_speedy = 5
b_square_directionx, b_square_directiony = 1, 1


bounce_sound = pg.mixer.Sound('sounds/bounce.mp3')

state = 0
r = 255
g, b = 0, 0

do_play = -1

pg.draw.rect(screen, 'Red', b_square_rectangle)
pg.draw.rect(screen, 'Black', b_square_rectangle, 1)
pg.display.update()

clock = pg.time.Clock()


def draw_move_bounce(red, green, blue):
    global b_square_directionx, b_square_directiony

    pg.draw.rect(screen, (red, green, blue), b_square_rectangle)
    pg.draw.rect(screen, 'Black', b_square_rectangle, 1, 1)

    b_square_rectangle.left += (b_square_speedx * b_square_directionx)
    b_square_rectangle.top += (b_square_speedy * b_square_directiony)

    if b_square_rectangle.right > 600 or b_square_rectangle.left < 0:
        bounce_sound.play()
        b_square_directionx *= -1

    if b_square_rectangle.bottom > 600 or b_square_rectangle.top < 0:
        bounce_sound.play()
        b_square_directiony *= -1

    pg.display.update()
    clock.tick(60)


def rainbow_rgb_code_generator():
    global r, g, b, state

    if state == 0:
        g += 5
        if g == 255:
            state = 1

    if state == 1:
        r -= 5
        if r == 0:
            state = 2

    if state == 2:
        b += 5
        if b == 255:
            state = 3

    if state == 3:
        g -= 5
        if g == 0:
            state = 4

    if state == 4:
        r += 5
        if r == 255:
            state = 5

    if state == 5:
        b -= 5
        if b == 0:
            state = 0


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
            do_play *= -1

    if do_play == 1:
        rainbow_rgb_code_generator()
        draw_move_bounce(r, g, b)
