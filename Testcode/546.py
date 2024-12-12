import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            while i < j and boxes[j] == boxes[j-1]:
                j -= 1
                k += 1
            if i == j:
                return (k+1)**2
            ans = (k+1)**2 + dp(i, j-1, 0)
            for m in range(j-1, i-1, -1):
                if boxes[m] == boxes[j]:
                    ans = max(ans, dp(i, m, k+1) + dp(m+1, j-1, 0))
            return ans

        return dp(0, len(boxes)-1, 0)

def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate random array of boxes
        length = random.randint(1, 100)  # 1 <= length <= 100
        boxes = [random.randint(1, 100) for _ in range(length)]  # 1 <= boxes[i] <= 100

        # Calculate expected output using the solution
        expected_output = solution.removeBoxes(boxes)

        # Add test case
        test_cases.append({
            "input": {"boxes": boxes},
            "output": expected_output
        })

    return test_cases

# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=100)

# Save the test cases to a JSON file
file_path = "../test_cases_546.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
