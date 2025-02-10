import pygame
import json
import os
import threading
import time
import argparse
import sys
from game_state import GAME_STATE

# Grid settings
GRID_SIZE = 40
MOVE_AMOUNT = GRID_SIZE  # Each move shifts one grid cell
MOVE_DELAY = 0.3  # Delay in seconds after each move


def load_level(filename):
    with open(filename, 'r') as f:
        level_data = json.load(f)
    return level_data


class Game:
    def __init__(self, level_file, width=None, height=None):
        pygame.init()

        # Load level data (coordinates in grid units)
        self.level_data = load_level(level_file)

        # If window size is not explicitly passed, try to get it from level data.
        # The level JSON can include a "window" property: [width, height]
        if width is None or height is None:
            window_size = self.level_data.get("window", None)
            if window_size:
                width, height = window_size
            else:
                width, height = (640, 480)

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Python Grid Game Framework")
        self.clock = pygame.time.Clock()
        self.running = True
        self.grid_size = GRID_SIZE

        # Load images from the "images" folder and scale them to GRID_SIZE x GRID_SIZE.
        current_dir = os.path.dirname(__file__)
        images_dir = os.path.join(current_dir, "images")

        # Load background images for the chess board pattern
        self.bg_stone = pygame.image.load(os.path.join(images_dir, "background_stone.png")).convert_alpha()
        self.bg_stone = pygame.transform.scale(self.bg_stone, (GRID_SIZE, GRID_SIZE))
        self.bg_dirt = pygame.image.load(os.path.join(images_dir, "background_dirt.png")).convert_alpha()
        self.bg_dirt = pygame.transform.scale(self.bg_dirt, (GRID_SIZE, GRID_SIZE))

        # Load other images
        self.player_image = pygame.image.load(os.path.join(images_dir, "player.png")).convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (GRID_SIZE, GRID_SIZE))

        self.coin_image = pygame.image.load(os.path.join(images_dir, "coin.png")).convert_alpha()
        self.coin_image = pygame.transform.scale(self.coin_image, (GRID_SIZE, GRID_SIZE))

        self.wall_image = pygame.image.load(os.path.join(images_dir, "wall.png")).convert_alpha()
        self.wall_image = pygame.transform.scale(self.wall_image, (GRID_SIZE, GRID_SIZE))

        self.goal_image = pygame.image.load(os.path.join(images_dir, "goal.png")).convert_alpha()
        self.goal_image = pygame.transform.scale(self.goal_image, (GRID_SIZE, GRID_SIZE))

        # Setup character (convert grid to pixels)
        self.character_pos = [coord * GRID_SIZE for coord in self.level_data.get("start", [0, 0])]

        # Convert walls: [grid_x, grid_y, grid_width, grid_height] -> pixels
        self.walls = []
        for wall in self.level_data.get("walls", []):
            self.walls.append([wall[0] * GRID_SIZE, wall[1] * GRID_SIZE, wall[2] * GRID_SIZE, wall[3] * GRID_SIZE])

        # Convert collectables: [grid_x, grid_y] -> pixels
        self.collectables = []
        for pos in self.level_data.get("collectables", []):
            self.collectables.append([pos[0] * GRID_SIZE, pos[1] * GRID_SIZE])

        # Convert goal: [grid_x, grid_y] -> pixels
        goal = self.level_data.get("goal", None)
        self.goal = [goal[0] * GRID_SIZE, goal[1] * GRID_SIZE] if goal else None

        self.collected = [False] * len(self.collectables)
        self.score = 0

        # Store the game instance and character position in the shared state
        GAME_STATE['game'] = self
        GAME_STATE['character_pos'] = self.character_pos

    def draw(self):
        # Draw the chess board background: tile the screen with alternating background images.
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        for x in range(0, screen_width, self.grid_size):
            for y in range(0, screen_height, self.grid_size):
                grid_x = x // self.grid_size
                grid_y = y // self.grid_size
                if (grid_x + grid_y) % 2 == 0:
                    self.screen.blit(self.bg_stone, (x, y))
                else:
                    self.screen.blit(self.bg_dirt, (x, y))

        # Draw walls: tile the wall image over each grid cell of the wall area.
        for wall in self.walls:
            grid_x = wall[0] // self.grid_size
            grid_y = wall[1] // self.grid_size
            grid_w = wall[2] // self.grid_size
            grid_h = wall[3] // self.grid_size
            for i in range(grid_w):
                for j in range(grid_h):
                    pos = ((grid_x + i) * self.grid_size, (grid_y + j) * self.grid_size)
                    self.screen.blit(self.wall_image, pos)

        # Draw collectables (coins)
        for i, pos in enumerate(self.collectables):
            if not self.collected[i]:
                self.screen.blit(self.coin_image, pos)

        # Draw goal
        if self.goal:
            self.screen.blit(self.goal_image, self.goal)

        # Draw player
        self.screen.blit(self.player_image, self.character_pos)

        pygame.display.flip()

    def update(self):
        # Check collisions with collectables
        char_rect = pygame.Rect(self.character_pos[0], self.character_pos[1],
                                self.grid_size, self.grid_size)
        for i, pos in enumerate(self.collectables):
            if not self.collected[i]:
                collect_rect = pygame.Rect(pos[0], pos[1], self.grid_size, self.grid_size)
                if char_rect.colliderect(collect_rect):
                    self.collected[i] = True
                    self.score += 1
                    print(f"Collected item {i + 1}! Score: {self.score}")

        # Check if reached goal
        if self.goal:
            goal_rect = pygame.Rect(self.goal[0], self.goal[1], self.grid_size, self.grid_size)
            if char_rect.colliderect(goal_rect):
                print("Goal reached!")
                self.running = False

    def game_loop(self):
        student_started = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
                      and not student_started):
                    student_main_function = GAME_STATE.get('student_main_function', None)
                    if student_main_function:
                        t = threading.Thread(target=student_main_function)
                        t.daemon = True
                        t.start()
                        student_started = True
                        print("Level code started!")
            self.update()
            self.draw()
            self.clock.tick(30)
        pygame.quit()

    def move_character(self, dx, dy):
        new_x = self.character_pos[0] + dx
        new_y = self.character_pos[1] + dy
        new_rect = pygame.Rect(new_x, new_y, self.grid_size, self.grid_size)
        collision = False
        for wall in self.walls:
            wall_rect = pygame.Rect(*wall)
            if new_rect.colliderect(wall_rect):
                collision = True
                break
        if not collision:
            self.character_pos[0] = new_x
            self.character_pos[1] = new_y
            GAME_STATE['character_pos'] = self.character_pos
        else:
            print("Collision with a wall!")


# --- Exposed API functions (student-facing) ---
def move_left():
    game = GAME_STATE.get('game')
    if game:
        game.move_character(-MOVE_AMOUNT, 0)
    time.sleep(MOVE_DELAY)


def move_right():
    game = GAME_STATE.get('game')
    if game:
        game.move_character(MOVE_AMOUNT, 0)
    time.sleep(MOVE_DELAY)


def move_up():
    game = GAME_STATE.get('game')
    if game:
        game.move_character(0, -MOVE_AMOUNT)
    time.sleep(MOVE_DELAY)


def move_down():
    game = GAME_STATE.get('game')
    if game:
        game.move_character(0, MOVE_AMOUNT)
    time.sleep(MOVE_DELAY)


def get_position():
    return GAME_STATE.get('character_pos')


def is_at_goal():
    """
    Returns True if the player's rectangle collides with the goal rectangle, else False.
    """
    game = GAME_STATE.get('game')
    if game and game.goal:
        char_rect = pygame.Rect(game.character_pos[0], game.character_pos[1], game.grid_size, game.grid_size)
        goal_rect = pygame.Rect(game.goal[0], game.goal[1], game.grid_size, game.grid_size)
        return char_rect.colliderect(goal_rect)
    return False


def is_not_at_goal():
    """
    Returns True as long as the player is not in the goal.
    """
    return not is_at_goal()


def is_wall_at_cell(grid_x, grid_y):
    """Helper function: returns True if the cell at (grid_x, grid_y) is occupied by a wall."""
    game = GAME_STATE.get('game')
    if game:
        cell_rect = pygame.Rect(grid_x * game.grid_size, grid_y * game.grid_size, game.grid_size, game.grid_size)
        for wall in game.walls:
            wall_rect = pygame.Rect(*wall)
            if cell_rect.colliderect(wall_rect):
                return True
    return False


def is_wall_left():
    game = GAME_STATE.get('game')
    if game:
        player_grid_x = game.character_pos[0] // game.grid_size
        player_grid_y = game.character_pos[1] // game.grid_size
        return is_wall_at_cell(player_grid_x - 1, player_grid_y)
    return False

def is_no_wall_left():
    return not is_wall_left()

def is_wall_right():
    game = GAME_STATE.get('game')
    if game:
        player_grid_x = game.character_pos[0] // game.grid_size
        player_grid_y = game.character_pos[1] // game.grid_size
        return is_wall_at_cell(player_grid_x + 1, player_grid_y)
    return False

def is_no_wall_right():
    return not is_wall_right()

def is_wall_up():
    game = GAME_STATE.get('game')
    if game:
        player_grid_x = game.character_pos[0] // game.grid_size
        player_grid_y = game.character_pos[1] // game.grid_size
        return is_wall_at_cell(player_grid_x, player_grid_y - 1)
    return False

def is_no_wall_up():
    return not is_wall_up()

def is_wall_down():
    game = GAME_STATE.get('game')
    if game:
        player_grid_x = game.character_pos[0] // game.grid_size
        player_grid_y = game.character_pos[1] // game.grid_size
        return is_wall_at_cell(player_grid_x, player_grid_y + 1)
    return False

def is_no_wall_down():
    return not is_wall_down()


# --- Main entry point with level number argument ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the grid game framework for a specific level."
    )
    parser.add_argument("level", type=int, nargs="?", default=1,
                        help="Level number to load (e.g., 1 for levels/level1.json and code/code_level1.py). Default is 1.")
    args = parser.parse_args()

    level_num = args.level
    current_dir = os.path.dirname(__file__)
    levels_dir = os.path.join(current_dir, "levels")
    level_file = os.path.join(levels_dir, f"level{level_num}.json")

    game = Game(level_file)

    # Add the "code" folder to sys.path so we can import code modules from there.
    code_dir = os.path.join(current_dir, "code")
    sys.path.insert(0, code_dir)

    code_module_name = f"code_level{level_num}"
    student_main_function = None
    try:
        code_module = __import__(code_module_name)
        if hasattr(code_module, "main"):
            student_main_function = code_module.main
    except ImportError:
        print(f"No code module found in '{code_dir}' with the name '{code_module_name}'. Running without student code.")

    GAME_STATE['student_main_function'] = student_main_function

    game.game_loop()
