import json
import random
from typing import List
from functools import lru_cache


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])  # dimensions
        walls = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "F":
                    food = (i, j)
                elif grid[i][j] == "C":
                    cat = (i, j)
                elif grid[i][j] == "M":
                    mouse = (i, j)
                elif grid[i][j] == "#":
                    walls.add((i, j))

        @lru_cache(None)
        def fn(cat, mouse, turn):
            if cat == food or cat == mouse or turn >= m * n * 2: return False
            if mouse == food: return True

            if not turn & 1:  # Mouse moving
                x, y = mouse
                for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                    for jump in range(0, mouseJump + 1):
                        xx, yy = x + jump * dx, y + jump * dy
                        if not (0 <= xx < m and 0 <= yy < n) or (xx, yy) in walls: break
                        if fn(cat, (xx, yy), turn + 1): return True
                return False
            else:  # Cat moving
                x, y = cat
                for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                    for jump in range(0, catJump + 1):
                        xx, yy = x + jump * dx, y + jump * dy
                        if not (0 <= xx < m and 0 <= yy < n) or (xx, yy) in walls: break
                        if not fn((xx, yy), mouse, turn + 1): return False
                return True

        return fn(cat, mouse, 0)


# Helper function to generate random grid
def generate_random_grid(rows, cols):
    if rows * cols < 3:
        raise ValueError("Grid must have at least 3 cells to place 'C', 'M', and 'F'.")

    grid = [["." for _ in range(cols)] for _ in range(rows)]

    # Place 'C', 'M', and 'F' in unique random positions
    positions = random.sample(range(rows * cols), 3)
    cx, cy = divmod(positions[0], cols)
    mx, my = divmod(positions[1], cols)
    fx, fy = divmod(positions[2], cols)

    grid[cx][cy] = "C"
    grid[mx][my] = "M"
    grid[fx][fy] = "F"

    # Place random walls
    wall_count = random.randint(0, (rows * cols) // 2)
    for _ in range(wall_count):
        wx, wy = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if grid[wx][wy] == ".":
            grid[wx][wy] = "#"

    return ["".join(row) for row in grid]

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        while True:
            rows = random.randint(1, 8)
            cols = random.randint(1, 8)
            if rows * cols >= 3:  # Ensure grid has at least 3 cells
                break

        grid = generate_random_grid(rows, cols)
        catJump = random.randint(1, 8)
        mouseJump = random.randint(1, 8)
        expected_output = solution.canMouseWin(grid, catJump, mouseJump)

        test_cases.append({
            "input": {"grid": grid, "catJump": catJump, "mouseJump": mouseJump},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1728.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
