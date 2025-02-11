# Aufgabe 11

In dieser Aufgabe ist bereits ein code vorgegeben:

```python
def main():

    # Do this without using any loops, except while is_not_at_goal() but as little code repetition as possible

    while is_not_at_goal():
        if is_no_wall_down():
            pick_up_coin()
            move_right()
        else:
            move_right()
```

Allerdings gibt es die `pick_up_coin()`

## Aufgabe

Deine Aufgabe ist es jetzt die `pick_up_coin()` methode zu erstellen.