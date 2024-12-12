import json
import random
from itertools import permutations
from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)

        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))

        from functools import cache

        @cache
        def fn(mask, j):
            """Return max score of assigning students in mask to first j mentors."""
            ans = 0
            for i in range(m):
                if not mask & (1 << i):
                    ans = max(ans, fn(mask ^ (1 << i), j - 1) + score[i][j])
            return ans

        return fn(1 << m, m - 1)


def generate_test_cases(num_cases=100, max_m=8, max_n=8):
    """Generate random test cases for the problem."""
    test_cases = []
    for _ in range(num_cases):
        m = random.randint(1, max_m)  # Number of students/mentors
        n = random.randint(1, max_n)  # Number of questions
        students = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
        mentors = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
        test_cases.append({"students": students, "mentors": mentors})
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the given test cases."""
    solution = Solution()
    outputs = []
    for case in test_cases:
        students = case["students"]
        mentors = case["mentors"]
        output = solution.maxCompatibilitySum(students, mentors)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=100)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": case, "output": output} for case, output in zip(test_cases, expected_outputs)]

with open("test_cases_1947.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
