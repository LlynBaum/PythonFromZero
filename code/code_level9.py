from main import move_left, move_right, move_up, move_down, get_position, is_not_at_goal


# This should be created by the schnuppi
def move_diagonal():
        move_down()
        move_right()


def main():

    # remember level5, maybe we can make it simple if we can create our own move method.

    while is_not_at_goal():
        move_diagonal()

    return
