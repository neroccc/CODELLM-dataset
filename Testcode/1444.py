import json
import random
from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        from functools import cache

        @cache
        def has_apple(start_row, start_col, end_row, end_col):
            for r in range(start_row, end_row+1):
                for c in range(start_col, end_col+1):
                    if pizza[r][c] == 'A':
                        return True
            return False

        @cache
        def dp(start_row, start_col, num_slices_left):
            if num_slices_left == 1:
                if has_apple(start_row, start_col, len(pizza)-1, len(pizza[0])-1):
                    return 1

            num_ways = 0
            for i in range(start_col+1, len(pizza[0])):
                if has_apple(start_row, start_col, len(pizza)-1, i-1):
                    num_ways += dp(start_row, i, num_slices_left-1)
            for j in range(start_row+1, len(pizza)):
                if has_apple(start_row, start_col, j-1, len(pizza[0])-1):
                    num_ways += dp(j, start_col, num_slices_left-1)
            return num_ways

        return dp(0, 0, k) % (10 ** 9 + 7)

# Helper function to generate random pizza matrices
def generate_pizza(rows, cols):
    return ["".join(random.choice(['A', '.']) for _ in range(cols)) for _ in range(rows)]

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        rows = random.randint(1, 50)
        cols = random.randint(1, 50)
        k = random.randint(1, min(10, rows * cols))
        pizza = generate_pizza(rows, cols)

        # Compute the expected output using the solution
        expected_output = solution.ways(pizza, k)

        test_cases.append({
            "input": {"pizza": pizza, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1444.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
