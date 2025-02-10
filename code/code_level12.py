from main import move_left, move_right, move_up, move_down, get_position, is_no_wall_down, is_not_at_goal, is_no_wall_up


# This should be created by the schnuppi
def go_down():
    while is_no_wall_down():
        move_down()


def go_up():
    while is_no_wall_up():
        move_up()


def pick_up_coin():
    # here
    return


def main():

    # Do this by only using while loops and also don't repeat code to go down and up, even if they are different lengths

    while is_not_at_goal():
        if is_no_wall_down():
            go_down()
            go_up()
            move_right()
        else:
            move_right()

    return
