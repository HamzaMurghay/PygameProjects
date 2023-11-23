import pygame as pg

screen = pg.display.set_mode((600, 600))
pg.display.set_icon(pg.image.load('graphics/8-Bit Pixel Game/back_arrow.png'))  # Change this
screen.fill('darkgrey')
clock = pg.time.Clock()

pg.init()

font = pg.font.SysFont('Consolas', 90)
matrix_font = pg.font.Font('fonts/garet/Garet-Book.ttf', 600)
br = matrix_font.render("[ ]", True, 'black')


lights = [0]*16

line1 = font.render(f"{' '.join(str(l) for l in lights[0:4])}", True, 'black')
line2 = font.render(f"{' '.join(str(l) for l in lights[4:8])}", True, 'black')
line3 = font.render(f"{' '.join(str(l) for l in lights[8:12])}", True, 'black')
line4 = font.render(f"{' '.join(str(l) for l in lights[12:16])}", True, 'black')


screen.blit(line1, (55, 95))
screen.blit(line2, (55, 195))
screen.blit(line3, (55, 295))
screen.blit(line4, (55, 395))

screen.blit(br, (-60, -150))


# first_seq = [1, 4, 7, 10, 13, 16]
# second_seq = [2, 5, 8, 11, 14]
# third_seq = [3, 6, 9, 12, 15]

temp_all = [
    [(0+num) % 16 for num in [4, 7, 10, 13, 16]],
    [(1+num) % 16 for num in [5, 8, 11, 14]],
    [(2+num) % 16 for num in [6, 9, 12, 15]],

    [(3 + num) % 16 for num in [1, 7, 10, 13, 16]],
    [(4 + num) % 16 for num in [2, 8, 11, 14]],
    [(5 + num) % 16 for num in [3, 9, 12, 15]],

    [(6 + num) % 16 for num in [1, 4, 10, 13, 16]],
    [(7 + num) % 16 for num in [2, 5, 11, 14]],
    [(8 + num) % 16 for num in [3, 6, 12, 15]],

    [(9 + num) % 16 for num in [1, 4, 7, 13, 16]],
    [(10 + num) % 16 for num in [2, 5, 8, 14]],
    [(11 + num) % 16 for num in [3, 6, 9, 15]],

    [(12 + num) % 16 for num in [1, 4, 7, 10, 16]],
    [(13 + num) % 16 for num in [2, 5, 8, 11]],
    [(14 + num) % 16 for num in [3, 6, 9, 12]],

    [(15 + num) % 16 for num in [1, 4, 7, 10, 13]],

]

print(temp_all)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYUP and event.key == pg.K_1:
            for light in temp_all[0]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_2:
            for light in temp_all[1]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_3:
            for light in temp_all[2]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_4:
            for light in temp_all[3]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_5:
            for light in temp_all[4]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_6:
            for light in temp_all[5]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_7:
            for light in temp_all[6]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_8:
            for light in temp_all[7]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_9:
            for light in temp_all[8]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_0:
            for light in temp_all[9]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_q:
            for light in temp_all[10]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_w:
            for light in temp_all[11]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_e:
            for light in temp_all[12]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_r:
            for light in temp_all[13]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_t:
            for light in temp_all[14]:
                lights[light] = int(not lights[light])

        if event.type == pg.KEYUP and event.key == pg.K_y:
            for light in temp_all[15]:
                lights[light] = int(not lights[light])

    screen.fill('darkgrey')

    line1 = font.render(f"{' '.join(str(l) for l in lights[0:4])}", True, 'black')
    line2 = font.render(f"{' '.join(str(l) for l in lights[4:8])}", True, 'black')
    line3 = font.render(f"{' '.join(str(l) for l in lights[8:12])}", True, 'black')
    line4 = font.render(f"{' '.join(str(l) for l in lights[12:16])}", True, 'black')

    screen.blit(line1, (75, 95))
    screen.blit(line2, (75, 195))
    screen.blit(line3, (75, 295))
    screen.blit(line4, (75, 395))

    screen.blit(br, (-60, -150))

    pg.display.update()
    clock.tick(60)
