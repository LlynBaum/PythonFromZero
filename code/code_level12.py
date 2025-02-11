from main import move_left, move_right, move_up, move_down, get_position, is_no_wall_down, is_not_at_goal, is_no_wall_up


# This should be created by the schnuppi
def pick_up_coin():
    while is_no_wall_down():
        move_down()
    while is_no_wall_up():
        move_up()


def main():

    # Do this without using any loops, except while is_not_at_goal() but as little code repetition as possible

    while is_not_at_goal():
        if is_no_wall_down():
            pick_up_coin()
            move_right()
        else:
            move_right()
