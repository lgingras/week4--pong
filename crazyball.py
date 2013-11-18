
# Crazyball
# It's a keep-away game!

import simplegui, random

# declare global variables - consts

WIDTH, HEIGHT = 200, 200
BALL_WIDTH, BALL_HEIGHT = 20, 50
HALF_BALL_WIDTH, HALF_BALL_HEIGHT = BALL_WIDTH / 2, BALL_HEIGHT / 2
PADDLE_WIDTH, PADDLE_HEIGHT = 50, 50
HALF_PADDLE_WIDTH, HALF_PADDLE_HEIGHT = PADDLE_WIDTH / 2, PADDLE_HEIGHT / 2
HIT = 10

### define event handlers
def new_game():
    # reset scores, reset pos and vel

    global ball_pos, ball_vel, paddle1_pos, paddle1_vel, score1, score2
    paddle1_pos = [WIDTH / 2, HEIGHT / 2]
    paddle1_vel = [5, 5]
    ball_pos = [ WIDTH / 5, HEIGHT / 5]
    ball_vel = [1, 1]
	score1, score2 = 0, 0

def draw(canvas):
    global ball_pos, ball_vel, paddle1_pos, score1

    # draw paddle
    canvas.draw_polygon([
        (paddle1_pos[0] - HALF_PADDLE_WIDTH, paddle1_pos[1] - HALF_PADDLE_HEIGHT), 
        (paddle1_pos[0] - HALF_PADDLE_WIDTH, paddle1_pos[1] + HALF_PADDLE_HEIGHT), 
        (paddle1_pos[0] + HALF_PADDLE_WIDTH, paddle1_pos[1] + HALF_PADDLE_HEIGHT), 
        (paddle1_pos[0] + HALF_PADDLE_WIDTH, paddle1_pos[1] - HALF_PADDLE_HEIGHT)], 
        3, "Red", "Red")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_polygon([
        (ball_pos[0] - HALF_BALL_WIDTH, ball_pos[1] - HALF_BALL_HEIGHT), 
        (ball_pos[0] - HALF_BALL_WIDTH, ball_pos[1] + HALF_BALL_HEIGHT), 
        (ball_pos[0] + HALF_BALL_WIDTH, ball_pos[1] + HALF_BALL_HEIGHT), 
        (ball_pos[0] + HALF_BALL_WIDTH, ball_pos[1] - HALF_BALL_HEIGHT)], 
        3, "White", "White")

	# bounce balls
    if ball_pos[0] <= HALF_BALL_WIDTH:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] >= WIDTH - HALF_BALL_WIDTH:
        ball_vel[0] = -ball_vel[0]

    if ball_pos[1] <= HALF_BALL_HEIGHT:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - HALF_BALL_HEIGHT:
        ball_vel[1] = -ball_vel[1]
    else:
    	ball_vel[1] = ball_vel[1]
        ball_vel[0] = ball_vel[0]
#########

    # print "what what"

	# collide ball off paddle 
	# collides ball off the left and right sides
	# hey girl, next time try setting the first two conditions as ==  
	# and then factor in the ball_vel for padding

    if ball_pos[0] + HALF_BALL_WIDTH >= paddle1_pos[0] - HALF_PADDLE_WIDTH and \
       ball_pos[0] - HALF_BALL_WIDTH <= paddle1_pos[0] + HALF_PADDLE_WIDTH and \
	   ball_pos[1] + HALF_BALL_HEIGHT >= paddle1_pos[1] - HALF_PADDLE_HEIGHT and \
	   ball_pos[1] - HALF_BALL_HEIGHT <= paddle1_pos[1] + HALF_PADDLE_HEIGHT:

	    if ball_pos[0] < paddle1_pos[0]: # ball comes in from left 
	    	x_overlap = (ball_pos[0] + HALF_BALL_WIDTH) - (paddle1_pos[0] - HALF_PADDLE_WIDTH) 
	    	print "ball comes in from left"
	    else:
	    	x_overlap = (paddle1_pos[0] + HALF_PADDLE_WIDTH) - (ball_pos[0] - HALF_BALL_WIDTH) # right
	    	print "ball comes in from right"

	    if ball_pos[1] < paddle1_pos[1]: 
	    	y_overlap = (paddle1_pos[1] - HALF_PADDLE_HEIGHT) - (ball_pos[1] + HALF_BALL_HEIGHT) # above
	    else:
	    	y_overlap = (ball_pos[1] - HALF_BALL_HEIGHT) - (paddle1_pos[1] + HALF_PADDLE_HEIGHT) # below

	    if x_overlap > y_overlap:
	    	ball_vel[0] = -ball_vel[0]

	    elif x_overlap < y_overlap:
	    	ball_vel[1] = -ball_vel[1]



	# try testing directionality






	# keep paddle inside the frame
 
	# I do not totally grok how to use max(min) and do not know why this doesn't work
	# paddle1_pos[0] = max(min(paddle1_pos[0] + paddle1_vel[0], WIDTH - HALF_PADDLE_WIDTH), HALF_PADDLE_WIDTH)
	# paddle1_pos[1] = max(min(paddle1_pos[1] + paddle1_vel[1], HEIGHT - HALF_PADDLE_HEIGHT), HALF_PADDLE_HEIGHT)

    if paddle1_pos[0] > WIDTH - HALF_PADDLE_WIDTH:
        paddle1_pos[0] = WIDTH - HALF_PADDLE_WIDTH
    elif paddle1_pos[0] < 0:
        paddle1_pos[0] = 0
    elif paddle1_pos[1] > HEIGHT - HALF_PADDLE_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PADDLE_HEIGHT
    elif paddle1_pos[1] < 0:
        paddle1_pos[1] = 0
 
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2, HEIGHT / 5), 20, "White")

def timer_handler():
	global score1
	score1 = score1 + 10 

# KEYUP AND KEYDOWN HANDLERS
def keydown(key):
    global paddle1_pos, paddle1_vel

    if key == simplegui.KEY_MAP["up"]:
        paddle1_pos[1] -= paddle1_vel[1] 
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_pos[1] += paddle1_vel[1] 
    elif key == simplegui.KEY_MAP["left"]:
        paddle1_pos[0] -= paddle1_vel[0] 
    elif key == simplegui.KEY_MAP["right"]:
        paddle1_pos[0] += paddle1_vel[0] 

def keyup(key):
    pass

# create frame and timer

frame = simplegui.create_frame("Crazyball", WIDTH, HEIGHT)
timer = simplegui.create_timer(1000, timer_handler)

### register event handlers

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button("Restart", new_game)

### start frame & timers

frame.start()
new_game()
timer.start()