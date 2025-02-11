# How this Project works

## Start the Project

YOu can start the Project by selecting a configuration for any level or with `python main.py 1` where the int 1 here is
the number for the level.

The program will the start the level that you selected. For this it chooses the `level{n}.json` and `code_level{n}.py`
and starts it up for you.

If the program is ready you can press `Space` to execute the code in the `code_level{n}.py` file.

## API for the student

You can find the code for this in the [main.py](./main.py) file below the Comment `# --- Exposed API functions (student-facing) ---`

Those are the methods available for the student. The methods will be explained during the Levels to the student.
For a short summary:

### Move the character

- `move_down()`
- `move_up()`
- `move_right()`
- `move_left()`

### Check for walls in a direction

- `is_no_wall_down()` and `is_wall_down()` -> `boolean`
- `is_no_wall_up()` and `is_wall_up()` -> `boolean`
- `is_no_wall_right()` and `is_wall_right()` -> `boolean`
- `is_no_wall_left()` and `is_wall_left()` -> `boolean`

### Is at the Exit Sign

- `is_at_goal()` -> `boolean`
- `is_not_at_goal()` -> `boolean`