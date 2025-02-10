from main import move_left, move_right, move_up, move_down, get_position, is_wall_left, is_no_wall_left, is_not_at_goal


def main():

    # that is a lot of repetition, this can be simplified by using a loop and a condition
    while is_not_at_goal():
        if is_no_wall_left():
            move_left()
            move_right()
            move_down()
        else:
            move_down()

    return
