import json
import random
from typing import List

class MyCircularQueue:
    def __init__(self, capacity: int) -> None:
        self.queue = [0] * capacity
        self.tailIndex = 0
        self.capacity = capacity

    def enQueue(self, value: int) -> None:
        self.queue[self.tailIndex] = value
        self.tailIndex = (self.tailIndex + 1) % self.capacity

    def get(self, index: int) -> int:
        return self.queue[index % self.capacity]

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = MyCircularQueue(cols)

        def get_min_health(currCell: int, nextRow: int, nextCol: int) -> int:
            if nextRow < 0 or nextCol < 0:
                return float("inf")
            index = cols * nextRow + nextCol
            nextCell = dp.get(index)
            return max(1, nextCell - currCell)

        for row in range(rows):
            for col in range(cols):
                currCell = dungeon[rows - row - 1][cols - col - 1]
                right_health = get_min_health(currCell, row, col - 1)
                down_health = get_min_health(currCell, row - 1, col)
                next_health = min(right_health, down_health)

                if next_health != float("inf"):
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp.enQueue(min_health)
        return dp.get(cols - 1)

def generate_random_dungeon(rows: int, cols: int, value_range=(-1000, 1000)) -> List[List[int]]:
    """
    Generates a random dungeon grid.

    :param rows: Number of rows in the dungeon.
    :param cols: Number of columns in the dungeon.
    :param value_range: Range of cell values in the dungeon.
    :return: Random dungeon grid.
    """
    return [[random.randint(value_range[0], value_range[1]) for _ in range(cols)] for _ in range(rows)]

def generate_test_cases(num_cases=100, max_rows=10, max_cols=10, value_range=(-1000, 1000)):
    """
    Generates test cases for the calculateMinimumHP function.

    :param num_cases: Number of test cases to generate.
    :param max_rows: Maximum number of rows in the dungeon.
    :param max_cols: Maximum number of columns in the dungeon.
    :param value_range: Range of cell values in the dungeon.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        rows = random.randint(1, max_rows)
        cols = random.randint(1, max_cols)
        dungeon = generate_random_dungeon(rows, cols, value_range)

        # Calculate the expected output using the provided solution
        expected_output = solution.calculateMinimumHP(dungeon)

        # Add test case
        test_cases.append({
            "input": dungeon,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_174.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_rows=10, max_cols=10)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
