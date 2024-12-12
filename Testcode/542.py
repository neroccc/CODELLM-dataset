import json
import random
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        Row, Col = len(mat), len(mat[0])
        queue = []
        directions = [[0, +1], [0, -1], [1, 0], [-1, 0]]

        for i in range(Row):
            for j in range(Col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = "*"

        for r, c in queue:
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <= row < Row and 0 <= col < Col and mat[row][col] == "*":
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))
        return mat

def generate_test_cases(solution, num_cases=10):
    test_cases = []

    for _ in range(num_cases):
        # Randomly generate dimensions for the matrix
        rows = random.randint(1, 10)  # Rows between 1 and 10 for manageable testing
        cols = random.randint(1, 10)  # Columns between 1 and 10
        mat = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

        # Ensure at least one zero exists in the matrix
        if all(all(cell == 1 for cell in row) for row in mat):
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            mat[x][y] = 0

        # Calculate the expected output using the provided solution
        expected_output = solution.updateMatrix([row[:] for row in mat])

        # Add test case
        test_cases.append({
            "input": {"mat": mat},
            "output": expected_output
        })

    return test_cases

# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=100)

# Save the test cases to a JSON file
file_path = "../test_cases_542.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
