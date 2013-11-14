# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
PAD_VELOCITY = 3
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = True
RIGHT = False

ball_vel = [3, 3]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]   
    horizontal_vel = random.randrange(120, 240) / 60
    vertical_vel = random.randrange(60, 180) / 60

    if direction == RIGHT:
        ball_vel = [horizontal_vel, -vertical_vel]
    elif direction == LEFT:
        ball_vel = [-horizontal_vel, -vertical_vel]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2

	spawn_ball(LEFT)

    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2

    paddle1_vel = 0
    paddle2_vel = 0

    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
 
    # collide and reflect off of left and right sides of canvas
 	if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
 		# paddle 1 hit:
 		if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT \
 			and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
 			ball_vel[0] *= -1.1
 		else:
		 	# paddle 1 miss:
 			score2 += 1
 			spawn_ball(RIGHT)

 	if ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH):
 		# paddle 2 hit:
 		if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT \
 			and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
 			ball_vel[0] *= -1.1
	 	# paddle 2 miss:
 		else:
 			score1 += 1
 			spawn_ball(LEFT)

    # top and bottom
    if ball_pos[1] <= BALL_RADIUS:
    	ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = max(min(paddle1_pos + paddle1_vel, HEIGHT-HALF_PAD_HEIGHT), 
    				  HALF_PAD_HEIGHT)
    paddle2_pos = max(min(paddle2_pos + paddle2_vel, HEIGHT-HALF_PAD_HEIGHT), 
    				  HALF_PAD_HEIGHT)

    # draw paddles
    c.draw_line((HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, (paddle1_pos + HALF_PAD_HEIGHT)), PAD_WIDTH, "Yellow")
    c.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, (paddle2_pos + HALF_PAD_HEIGHT)), PAD_WIDTH, "Yellow")

    # draw scores
    c.draw_text(str(score1), (WIDTH / 4, 50), 40, "White")
    c.draw_text(str(score2), (3 * (WIDTH / 4), 50), 40, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += -PAD_VELOCITY
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += PAD_VELOCITY

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += -PAD_VELOCITY
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += PAD_VELOCITY

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += PAD_VELOCITY
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += -PAD_VELOCITY

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += PAD_VELOCITY
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += -PAD_VELOCITY

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
