import json
import random
from itertools import accumulate


class Solution:
    def stoneGameVIII(self, stones):
        ps = list(accumulate(stones))
        ans = ps[-1]
        for num in ps[::-1][1:-1]:
            ans = max(ans, num - ans)
        return ans


# Function to generate random test cases
def generate_test_cases(num_cases=50, max_n=10 ** 5, max_stone_value=10 ** 4):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate a random number of stones
        n = random.randint(2, min(max_n, 1000))  # Limited to smaller n for testing
        stones = [random.randint(-max_stone_value, max_stone_value) for _ in range(n)]

        # Calculate the expected output using the provided solution
        expected_output = solution.stoneGameVIII(stones)

        test_cases.append({
            "input": {"stones": stones},
            "output": expected_output
        })

    # Save the test cases to a JSON file
    with open("test_cases_1872.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
generate_test_cases()
