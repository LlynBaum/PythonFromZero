from main import move_left, move_right, move_up, move_down, get_position, is_no_wall_right, is_no_wall_left, \
    is_not_at_goal


def main():

    # the same as level 7 but this time we can also go to the other side
    while is_not_at_goal():
        if is_no_wall_left():
            move_left()
            move_right()
            move_down()
        elif is_no_wall_right():
            move_right()
            move_left()
            move_down()
        else:
            move_down()

    return
