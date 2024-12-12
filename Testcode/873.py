import json
import random
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        longest = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                length = 2

                while a + b in nums:
                    a, b = b, a + b
                    length += 1

                if length > 2 and length > longest:
                    longest = length

        return longest


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random length for the array
        length = random.randint(3, 100)  # Keep lengths manageable for computation
        # Generate a sorted array of unique random integers
        arr = sorted(random.sample(range(1, 10**5), length))
        # Compute the output using the solution's method
        output = solution.lenLongestFibSubseq(arr)
        # Append the test case
        test_cases.append({
            "input": {
                "arr": arr
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_873.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
