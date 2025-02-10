from main import move_left, move_right, move_up, move_down, get_position, is_not_at_goal


def main():

    # That is a long way to walk, can this not be made easier? Counting is also annoying

    while is_not_at_goal():
        move_down()

    return
