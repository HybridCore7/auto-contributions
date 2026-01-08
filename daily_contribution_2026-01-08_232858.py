# Python: Generates a simple maze using a randomized Prim's algorithm and visualizes it.

import random

def create_maze(width, height):
    """Generates a maze using a randomized Prim's algorithm."""
    maze = [['#' for _ in range(width)] for _ in range(height)]
    start_x, start_y = random.randint(0, (width - 1) // 2) * 2 + 1, random.randint(0, (height - 1) // 2) * 2 + 1
    maze[start_y][start_x] = ' '
    walls = []

    def add_walls(x, y):
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx * 2, y + dy * 2
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == '#':
                walls.append(((x + dx, y + dy), (nx, ny)))

    add_walls(start_x, start_y)

    while walls:
        (wall_x, wall_y), (next_x, next_y) = random.choice(walls)
        walls.remove(((wall_x, wall_y), (next_x, next_y)))

        if maze[next_y][next_x] == '#':
            maze[wall_y][wall_x] = ' '
            maze[next_y][next_x] = ' '
            add_walls(next_x, next_y)
    return maze

def print_maze(maze):
    """Prints the maze to the console."""
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    maze_width = 41
    maze_height = 21
    generated_maze = create_maze(maze_width, maze_height)
    print_maze(generated_maze)