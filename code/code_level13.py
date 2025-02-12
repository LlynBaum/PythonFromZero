from main import *

def try_move_to_side():
    if is_no_wall_down():
        move_down()
    else:
        if is_no_wall_up():
            move_up()

def main():

    while is_not_at_goal():
        try_move_to_side()
        move_right()

# Solution for Challenge
def main_challenge():
    while is_not_at_goal():
        try_move_to_side()
        if is_no_wall_right():
            move_right()