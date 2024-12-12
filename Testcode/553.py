import json
from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            return str(nums[0]) + "/(" + "/".join([str(num) for num in nums[1:]]) + ")"


def generate_test_cases(num_cases=100):
    import random

    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Randomly generate the size of the array (1 to 10 as per constraints)
        size = random.randint(1, 10)
        # Randomly generate the array elements (2 to 1000 as per constraints)
        nums = [random.randint(2, 1000) for _ in range(size)]
        # Compute the output using the solution's method
        output = solution.optimalDivision(nums)
        # Append the test case
        test_cases.append({"input": {"nums": nums}, "output": output})

    # Save to a JSON file
    with open("../test_cases_553.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
