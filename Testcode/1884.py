import json
import math
import random
from functools import lru_cache


class Solution:
    def twoEggDrop(self, n: int) -> int:
        # x2 + x - 2n = 0 -- >  = (-b2 +- srt(b2-4ac))/2
        # (-1 +(sqr1+4*c))/2
        ans = ((1+8*n)**0.5 -1)/2
        return math.ceil(ans)

# Function to generate test cases
def generate_test_cases(num_cases=50, max_floors=1000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate a random number of floors
        n = random.randint(1, max_floors)

        # Compute the expected output using the solution
        expected_output = solution.twoEggDrop(n)

        # Add test case to the list
        test_cases.append({
            "input": {"n": n},
            "output": expected_output
        })

    # Save test cases to a JSON file
    with open("test_cases_1884.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
generate_test_cases()
