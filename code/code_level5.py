from main import move_left, move_right, move_up, move_down, get_position, is_not_at_goal


def main():

    # Now you have to travel a long distance in two directions. Maybe you can modify the code from last
    # Level to also travel in another direction

    while is_not_at_goal():
        move_down()
        move_right()

    return
