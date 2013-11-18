# packrat code

    canvas.draw_circle((10, 10), 12, 4, "Red")
    canvas.draw_circle((100, 10), 12, 4, "Yellow")
    canvas.draw_circle((100, 100), 12, 4, "Blue")
    canvas.draw_circle((10, 100), 12, 4, "Green")
	ball = [[10, 10], [100, 10], [100, 100], [10, 100]]
#	ball = [(10,10), (100, 10), (100, 100), (10,100)]
# packrat code
    canvas.draw_polygon(ball, BALL_SIZE, "Red")

    canvas.draw_circle((10, 10), 12, 4, "White")
    canvas.draw_circle((100, 10), 12, 4, "Yellow")
#    canvas.draw_circle((100, 100), 12, 4, "Blue")
 #   canvas.draw_circle((10, 100), 12, 4, "Green")
# try with circle
	global paddle_pos, ball_vel
# 	WORKED! try with circle
	# canvas.draw_circle(paddle_pos, 20, 3, "Red")

#now try with line
# WORKED!
	# canvas.draw_line((ball_pos[0], ball_pos[1]), \
	# 	(ball_pos[0], ball_pos[1] + HALF_BALL_HEIGHT), 3, "Red" )

	print ball_pos

#now try with polygon


#working but just on vertial
	if ball_pos[0] + HALF_BALL_WIDTH >= paddle1_pos[0] - HALF_PADDLE_WIDTH \
	and ball_pos[0] - HALF_BALL_WIDTH <= paddle1_pos[0] + HALF_PADDLE_WIDTH:
		ball_vel[0] = -ball_vel[0]
	else:
		ball_vel[0] = ball_vel[0]

	if ball_pos[0] > paddle1_pos[0] - HALF_PADDLE_WIDTH \
	and ball_pos[1] > paddle1_pos[1] - half_paddle
		ball_vel[0] = -ball_vel[0]
	else:
		ball_vel[0] = ball_vel[0]


		#closest working
			if ball_pos[0] + HALF_BALL_WIDTH >= paddle1_pos[0] - HALF_PADDLE_WIDTH \
	and ball_pos[0] - HALF_BALL_WIDTH <= paddle1_pos[0] + HALF_PADDLE_WIDTH \
	and ball_pos[1] + HALF_BALL_HEIGHT >= paddle1_pos[1] - HALF_PADDLE_HEIGHT \
	and ball_pos[1] - HALF_BALL_HEIGHT <= paddle1_pos[1] + HALF_PADDLE_HEIGHT:
		ball_vel[0] = -ball_vel[0]
		ball_vel[1] = -ball_vel[1]
	else:
		ball_vel[0] = ball_vel[0]