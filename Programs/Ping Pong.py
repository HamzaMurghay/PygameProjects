import pygame as pg
import random

# Setting up Pygame Pre-Requisites -----------------------------------------------------------------------------

screen = pg.display.set_mode((1000, 500))
pg.display.set_caption("Ping Pong")
clock = pg.time.Clock()

pg.init()

# Setting Up Game Objects --------------------------------------------------------------------------------------

paddle1 = pg.rect.Rect(10, 215, 10, 70)
paddle2 = pg.rect.Rect(980, 215, 10, 70)

ball = pg.transform.scale(pg.image.load('../assets/graphics/Ping Pong/ping_pong_ball_trimmed.png').convert_alpha(), (30, 30))


text_font = pg.font.SysFont("Joker", 50)
start_prompt = text_font.render("Press Space to start", True, (255, 255, 255))

game_score = [0, 0]
score_board = text_font.render(f"{game_score[0]}     {game_score[1]}", True, (255, 255, 255))

# Setting up Game Variables ------------------------------------------------------------------------------------

ball_position = pg.math.Vector2(485, 235)
ball_direction = pg.math.Vector2([-1, 1][random.random() > 0.5] * random.randint(300, 1000)/1000,
                                 [-1, 1][random.random() > 0.5] * random.randint(0, 800) / 1000).normalize()

ball_speed = 14
paddle_speed = 12

start = 0

# Defining Functions -------------------------------------------------------------------------------------------


def create_new_round():
    global ball_position, ball_direction, start, score_board

    game_score[ball_position.x < -30] += 1
    score_board = text_font.render(f"{game_score[0]}     {game_score[1]}", True, (255, 255, 255))

    start = 0

    ball_position = pg.math.Vector2(485, 235)
    ball_direction = pg.math.Vector2([-1, 1][random.random() > 0.5] * random.randint(300, 1000) / 1000,
                                     [-1, 1][random.random() > 0.5] * random.randint(0, 800) / 1000).normalize()


def handle_player_input():
    keys = pg.key.get_pressed()

    if keys[pg.K_w] and paddle1.y > 0:
        paddle1.y -= paddle_speed
    elif keys[pg.K_s] and paddle1.y < 430:
        paddle1.y += paddle_speed

    if keys[pg.K_UP] and paddle2.y > 0:
        paddle2.y -= paddle_speed
    elif keys[pg.K_DOWN] and paddle2.y < 430:
        paddle2.y += paddle_speed


def ball_movement(ball_pos, ball_dir):
    if not start:
        return

    ball_pos += ball_speed * ball_dir

    if not 0 < ball_pos.y < 470:
        ball_dir.y *= -1

    if ball_pos.x < 24 and (paddle1.y < ball_pos.y-15 < paddle1.y + 70 or paddle1.y < ball_pos.y+15 < paddle1.y + 70):
        ball_dir.x *= -1
    if ball_pos.x > 935 and (paddle2.y < ball_pos.y-15 < paddle2.y + 70 or paddle2.y < ball_pos.y-15 < paddle2.y + 70):
        ball_dir.x *= -1

    if not -30 < ball_pos.x < 1000:
        create_new_round()


def draw_elements():
    pg.draw.line(screen, 'white', (500, 0), (500, 500))

    pg.draw.rect(screen, (100, 100, 100), paddle1, border_radius=10)
    pg.draw.rect(screen, (100, 100, 100), paddle2, border_radius=10)

    screen.blit(ball, ball_position)
    screen.blit(score_board, (458, 20))

    if not start:
        screen.blit(start_prompt, (338, 180))


# Main Loop ----------------------------------------------------------------------------------------------------

while True:
    screen.fill('black')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not start:
            start = 1

    handle_player_input()
    draw_elements()
    ball_movement(ball_position, ball_direction)

    pg.display.update()
    clock.tick(60)
