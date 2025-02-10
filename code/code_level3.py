from main import move_left, move_right, move_up, move_down, get_position


def main():

    # Move the player to the exit sign, but you can't walk through wooden boxes
    move_down()
    move_down()
    move_right()
    move_down()

    return
