from main import *

def try_move_to_side():
    if is_no_wall_down():
        move_down()
    else:
        if is_no_wall_up():
            move_up()

def main():

    # hier kommt dein code
    think("Darki")
    think(19)
    think("Darki 19")

    move_right()