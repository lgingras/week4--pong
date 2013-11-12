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


