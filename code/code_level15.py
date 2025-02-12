from main import *

def try_move_to_side():
    if is_no_wall_down():
        move_down()
    else:
        if is_no_wall_up():
            move_up()

def main():

    # hier kommt dein code
    think(19 + 10)
    think(19 - 9)
    think(19 * 2)
    think(19 / 2)

    move_right()