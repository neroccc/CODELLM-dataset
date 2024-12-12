import json
import random
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        res = 0
        for num in arr:
            while stack and stack[-1] <= num:
                cur = stack.pop()
                if stack:
                    res += cur * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


def generate_test_cases(num_cases: int = 100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate random array size within the allowed range
        array_size = random.randint(2, 40)
        # Generate random array values within the allowed range
        arr = [random.randint(1, 15) for _ in range(array_size)]
        # Calculate the output using the solution
        output = solution.mctFromLeafValues(arr)
        # Store the test case
        test_cases.append({"input": arr, "output": output})

    # Add edge cases
    edge_cases = [
        {"input": [1, 1], "output": solution.mctFromLeafValues([1, 1])},  # Minimal case
        {"input": [15] * 40, "output": solution.mctFromLeafValues([15] * 40)},  # Maximum array size
        {"input": [1, 15], "output": solution.mctFromLeafValues([1, 15])},  # Min and max values
        {"input": [1, 2, 3, 4], "output": solution.mctFromLeafValues([1, 2, 3, 4])},  # Ascending order
        {"input": [4, 3, 2, 1], "output": solution.mctFromLeafValues([4, 3, 2, 1])},  # Descending order
    ]

    test_cases.extend(edge_cases)

    # Save to a file
    with open("test_case_1130.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save 1000 test cases
generate_test_cases()
