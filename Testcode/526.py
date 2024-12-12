import json
from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        self.count = 0

        def backtrack(start):
            if start == n:
                self.count += 1
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                if nums[start] % (start + 1) == 0 or (start + 1) % nums[start] == 0:
                    backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return self.count


def generate_test_cases(solution, num_cases=15):
    test_cases = []

    for n in range(1, num_cases + 1):
        # Generate input and expected output
        expected_output = solution.countArrangement(n)
        test_cases.append({
            "input": {"n": n},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=15)

# Save the test cases to a JSON file
file_path = "../test_cases_526.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
