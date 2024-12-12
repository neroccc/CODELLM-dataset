import json
import random
from typing import List

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        my_set = set(A)
        curr = 0
        prev = set()
        prev.add(A[0])
        for num in A[1:]:
            temp = set()
            for p in prev:
                temp.add(num | p)
                my_set.add(num | p)
            prev = temp
            prev.add(num)

        return len(my_set)


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random length for the array
        length = random.randint(1, 100)  # Limit length for practical execution
        # Generate an array of random integers
        arr = [random.randint(0, 10**9) for _ in range(length)]

        # Compute the output using the solution's method
        output = solution.subarrayBitwiseORs(arr)
        # Append the test case
        test_cases.append({
            "input": {
                "arr": arr
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_898.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
