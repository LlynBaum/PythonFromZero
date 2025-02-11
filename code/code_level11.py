from main import *


def main():

    while is_not_at_goal():
        if is_no_wall_down():
            pick_up_coin()
            move_right()
        else:
            move_right()

# hier kommt dein code
