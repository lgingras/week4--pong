
# Crazyball
# It's a keep-away game!

import simplegui
import random

# declare global variables - consts

WIDTH, HEIGHT = 400, 400
BALL_WIDTH, BALL_HEIGHT = 20, 50
HALF_BALL_WIDTH, HALF_BALL_HEIGHT = BALL_WIDTH / 2, BALL_HEIGHT / 2
PADDLE_WIDTH, PADDLE_HEIGHT = 50, 50
HALF_PADDLE_WIDTH, HALF_PADDLE_HEIGHT = PADDLE_WIDTH / 2, PADDLE_HEIGHT / 2

### define event handlers
def new_game():
    # reset scores, reset pos and vel

    global ball_pos, ball_vel, paddle1_pos, paddle1_vel
    paddle1_pos = [WIDTH / 2, HEIGHT / 2]
    paddle1_vel = [3, 3]
    ball_pos = [ WIDTH / 5, HEIGHT / 5]
    ball_vel = [1, 1]

    score1, score2 = 0, 0

def draw(canvas):
	global ball_pos, ball_vel

 	# draw paddle
	canvas.draw_polygon([\
		(paddle1_pos[0] - HALF_PADDLE_WIDTH, paddle1_pos[1] - HALF_PADDLE_HEIGHT), \
		(paddle1_pos[0] - HALF_PADDLE_WIDTH, paddle1_pos[1] + HALF_PADDLE_HEIGHT), \
		(paddle1_pos[0] + HALF_PADDLE_WIDTH, paddle1_pos[1] + HALF_PADDLE_HEIGHT), \
		(paddle1_pos[0] + HALF_PADDLE_WIDTH, paddle1_pos[1] - HALF_PADDLE_HEIGHT)], \
		3, "Red", "Red")

	# update ball
	ball_pos[0] += ball_vel[0]
	ball_pos[1] += ball_vel[1]

	# draw ball
	canvas.draw_polygon([\
		(ball_pos[0] - HALF_BALL_WIDTH, ball_pos[1] - HALF_BALL_HEIGHT), \
		(ball_pos[0] - HALF_BALL_WIDTH, ball_pos[1] + HALF_BALL_HEIGHT), \
		(ball_pos[0] + HALF_BALL_WIDTH, ball_pos[1] + HALF_BALL_HEIGHT), \
		(ball_pos[0] + HALF_BALL_WIDTH, ball_pos[1] - HALF_BALL_HEIGHT)], \
		3, "White", "White")


	# bounce ball off sides 
	if ball_pos[0] <= HALF_BALL_WIDTH:
		ball_vel[0] = -ball_vel[0]
	elif ball_pos[0] >= WIDTH - HALF_BALL_WIDTH:
		ball_vel[0] = -ball_vel[0]

	# if HALF_BALL_WIDTH >= ball_pos[0] >= WIDTH - HALF_BALL_WIDTH:
	# 	ball_vel[0] = -ball_vel[0]

	if ball_pos[1] <= HALF_BALL_HEIGHT:
		ball_vel[1] = -ball_vel[1]
	elif ball_pos[1] >= HEIGHT - HALF_BALL_HEIGHT:
		ball_vel[1] = -ball_vel[1]

# collide ball off paddle
	if ((ball_pos[0] + HALF_BALL_WIDTH > paddle1_pos[0] - HALF_PADDLE_WIDTH) \
	or (ball_pos[0] - HALF_BALL_WIDTH < paddle1_pos[0] + HALF_PADDLE_WIDTH)) \
	and ball_pos[1] + HALF_BALL_WIDTH > paddle1_pos[1] - HALF_PADDLE_HEIGHT \
	and ball_pos[1] - HALF_BALL_HEIGHT < paddle1_pos[1] + HALF_PADDLE_HEIGHT: \
			ball_vel[0] = -ball_vel[0]

# KEYUP AND KEYDOWN HANDLERS
def keydown(key):
	global paddle1_pos, paddle1_vel

    if key == simplegui.KEY_MAP["up"]:
		paddle1_pos[1] -= paddle1_vel[1] * 5
    elif key == simplegui.KEY_MAP["down"]:
    	paddle1_pos[1] += paddle1_vel[1] * 5
    elif key == simplegui.KEY_MAP["left"]:
    	paddle1_pos[0] -= paddle1_vel[0] * 5
    elif key == simplegui.KEY_MAP["right"]:
    	paddle1_pos[0] += paddle1_vel[0] * 5

def keyup(key):
    pass

# create frame

frame = simplegui.create_frame("Crazyball", 400, 400)

### register event handlers

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

restart_button = frame.add_button("Restart", new_game)


# keyup, keydown, restart, frame

### start frame & timers

frame.start()
new_game()