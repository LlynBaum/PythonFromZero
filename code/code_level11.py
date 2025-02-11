from main import move_left, move_right, move_up, move_down, get_position, is_no_wall_down, is_not_at_goal


def main():

    while is_not_at_goal():
        if is_no_wall_down():
            pick_up_coin()
            move_right()
        else:
            move_right()

# hier kommt dein code
