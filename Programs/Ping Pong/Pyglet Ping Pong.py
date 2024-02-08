import math
import random
import pyglet as pl
from pyglet.window import key

# Setting up Pyglet Pre-Requisites -----------------------------------------------------------------------------

window = pl.window.Window(width=1000, height=500)
window.set_caption("Ping Pong")

keys = key.KeyStateHandler()
window.push_handlers(keys)

batch = pl.graphics.Batch()


@window.event
def on_draw():
    window.clear()

    score.text = f"{game_score[0]}         {game_score[1]}"
    batch.draw()

    if not start:
        start_prompt.draw()

# Defining Functions -------------------------------------------------------------------------------------------


def generate_random_angle():
    ball_angle = (0, 180)[random.random() > 0.5]
    ball_angle += random.randint(-56, 56)

    return math.radians(ball_angle)


def create_new_round(winner):
    global start, ball_speed, bounce_counter, game_score

    game_score[winner] += 1
    start = 0

    ball_speed = 700
    bounce_counter = 0

    ball.x = 500
    ball.y = 250

    ball_direction_temp = ball_direction.from_heading(generate_random_angle())

    ball_direction.x = ball_direction_temp.x
    ball_direction.y = ball_direction_temp.y


def handle_player_input(dt):
    global start

    if keys[key.SPACE] and not start:
        start = 1

    if keys[key.W] and paddle1.y < 430:
        paddle1.y += paddle_speed
    if keys[key.S] and paddle1.y > 0:
        paddle1.y -= paddle_speed

    if keys[key.UP] and paddle2.y < 430:
        paddle2.y += paddle_speed
    if keys[key.DOWN] and paddle2.y > 0:
        paddle2.y -= paddle_speed


def ball_movement(dt):
    if not start:
        return

    global bounce_counter, ball_speed

    if bounce_counter > 4:
        ball_speed = 700 + speed_increase * (bounce_counter - 4)

    ball.position = pl.math.Vec2(*ball.position) + ball_direction * ball_speed * dt

    # Bouncing if collisions take place -----------------------------------------------------------------------------

    if ball.y > 480 or ball.y < 20:
        ball_direction.y *= -1

    if 40 > ball.x > 15 and paddle1.y < ball.y < paddle1.y + 70:
        ball_direction.x *= -1
        bounce_counter += 1

    if 960 < ball.x < 985 and paddle2.y < ball.y < paddle2.y + 70:
        ball_direction.x *= -1
        bounce_counter += 1

    if (paddle1.y + 70 > ball.y + 15 > paddle1.y or paddle1.y < ball.y - 15 < paddle1.y + 70) and ball.x < 15:
        ball_direction.y *= -1

    if (paddle2.y + 70 > ball.y + 15 > paddle2.y or paddle2.y < ball.y - 15 < paddle2.y + 70) and 985 < ball.x:
        ball_direction.y *= -1

    # Creating new round when ball passes borders ---------------------------------------------------------------

    if ball.x < 0:
        create_new_round(1)
    elif ball.x > 1000:
        create_new_round(0)


# Setting up Game Elements -------------------------------------------------------------------------------------

line = pl.shapes.Line(500, 0, 500, 500, batch=batch)

paddle1 = pl.shapes.Rectangle(10, 215, 10, 70, color=(100, 100, 100), batch=batch)
paddle2 = pl.shapes.Rectangle(980, 215, 10, 70, color=(100, 100, 100), batch=batch)

ball = pl.shapes.Circle(500, 250, 15, color=(255, 0, 0), batch=batch)

start_prompt = pl.text.Label("Press Space to start", x=332, y=290, font_size=30)

game_score = [0, 0]
score = pl.text.Label(f"{game_score[0]}    {game_score[1]}", x=320, y=400, font_size=75, batch=batch)

# Setting up Game Variables ------------------------------------------------------------------------------------

paddle_speed = 15

ball_direction = pl.math.Vec2(0, 1).from_heading(generate_random_angle())
ball_speed = 700

bounce_counter = 0
speed_increase = 100

start = 0

# Scheduling ---------------------------------------------------------------------------------------------------

pl.clock.schedule_interval(handle_player_input, 1 / 60)
pl.clock.schedule_interval(ball_movement, 1 / 80)

pl.app.run()
