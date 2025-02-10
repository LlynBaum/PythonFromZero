from main import move_left, move_right, move_up, move_down, get_position, is_no_wall_down, is_not_at_goal


# This should be created by the schnuppi
def go_down():
    for i in range(7):
        move_down()

def go_up():
    for i in range(7):
        move_up()


def main():

    # remember level5, maybe we can make it simple if we can create our own move method.

    while is_not_at_goal():
        if is_no_wall_down():
            go_down()
            go_up()
            move_right()
        else:
            move_right()

    return
