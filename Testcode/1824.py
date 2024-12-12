import json
import random
import sys
from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        a, b, c = 1, 0, 1
        for i in range(1, n):
            a = a if obstacles[i] != 1 else sys.maxsize
            b = b if obstacles[i] != 2 else sys.maxsize
            c = c if obstacles[i] != 3 else sys.maxsize
            if obstacles[i] != 1:
                a = min(a, b + 1 if obstacles[i] != 2 else sys.maxsize, c + 1 if obstacles[i] != 3 else sys.maxsize)
            if obstacles[i] != 2:
                b = min(b, a + 1 if obstacles[i] != 1 else sys.maxsize, c + 1 if obstacles[i] != 3 else sys.maxsize)
            if obstacles[i] != 3:
                c = min(c, a + 1 if obstacles[i] != 1 else sys.maxsize, b + 1 if obstacles[i] != 2 else sys.maxsize)
        return min(a, b, c)

# Helper function to generate random obstacles array
def generate_random_obstacles(n, obstacle_chance=0.3):
    obstacles = [0] * (n + 1)
    for i in range(1, n):  # Exclude first and last position
        if random.random() < obstacle_chance:
            obstacles[i] = random.randint(1, 3)
    return obstacles

# Generate test cases
def generate_test_cases(num_cases=50, max_n=500_000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, min(1000, max_n))  # For performance, cap n at 1000 for generation
        obstacles = generate_random_obstacles(n)
        expected_output = solution.minSideJumps(obstacles)

        test_cases.append({
            "input": {"obstacles": obstacles},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1824.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save test cases
generate_test_cases()
