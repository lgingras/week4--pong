	reflect on the y-axis
    if ball_pos[1] - HALF_BALL_HEIGHT <= paddle1_pos[1] + HALF_PADDLE_HEIGHT \
    and ball_pos[1] + HALF_BALL_HEIGHT >= paddle1_pos[1] - HALF_PADDLE_HEIGHT \
    and ball_pos[0] + HALF_BALL_WIDTH >= paddle1_pos[0] - HALF_PADDLE_WIDTH \
    and ball_pos[0] - HALF_BALL_WIDTH <= paddle1_pos[0] + HALF_PADDLE_WIDTH:
        ball_vel[1] *= -1.1
        score1 -= HIT
