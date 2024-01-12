import pygame as pg
from math import sin, cos, radians, degrees, pi

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('../graphics/8-Bit Pixel Game/back_arrow.png'))  # Change this
screen.fill('darkgrey')

pg.init()

light_source = pg.draw.circle(screen, 'white', (50, 50), 30)
mirror1 = pg.image.load('../../graphics/8-Bit Pixel Game/lvl1/line_mirror.png').convert_alpha()
# s, t = mirror1.get_rect(topleft=(500, 300)).left, mirror1.get_rect(topleft=(500, 300)).top
centerx = mirror1.get_rect(topleft=(500, 300)).centerx
centery = mirror1.get_rect(topleft=(500, 300)).centery
radius = centery - 300

x = centerx + (radius*sin(-90*pi/180))
y = centery + (radius*cos(-90*pi/180))


mirror1_rotated = pg.transform.rotate(mirror1, 80)
mirror1_rotated_rect = mirror1_rotated.get_rect(center=mirror1.get_rect(topleft=(500, 300)).center)

# circle = pg.draw.circle(screen, 'yellow', (504, 364), 64, 1)
pg.draw.rect(screen, 'pink', mirror1_rotated_rect)
screen.blit(mirror1, (500, 300))
screen.blit(mirror1_rotated, mirror1_rotated_rect)

# pg.draw.arc(screen, 'yellow', (440, 300, 120, 120), pi, 3*pi/2)

pg.draw.line(screen, 'yellow', (500, 300), (x, y))

# def create_mirror(start_posit, end_posit):
#     mirror = pg.draw.line(screen, 'white', start_posit, end_posit, 1)
#     mirror_slope = (mirror.top - mirror.bottom)/(mirror.right - mirror.left)
#     b = (300 - 500*mirror_slope)
#     mirror_points = []
#     for x in range(500, 479, -1):
#         y = mirror_slope*x + b
#         mirror_points.append((x, y))
#     return mirror, mirror_points


# mirror1, mirror1_points = create_mirror()


# print(circle)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            ray = pg.draw.line(screen, 'yellow', light_source.center, pg.mouse.get_pos())
            if ray.colliderect(mirror1_rotated_rect):
                print('collide')

    pg.display.update()
