import json
import random
from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        subsets = []
        self.ans = len(tasks)

        def func(idx):
            if len(subsets) >= self.ans:
                return

            if idx == len(tasks):
                self.ans = min(self.ans, len(subsets))
                return

            for i in range(len(subsets)):
                if subsets[i] + tasks[idx] <= sessionTime:
                    subsets[i] += tasks[idx]
                    func(idx + 1)
                    subsets[i] -= tasks[idx]

            subsets.append(tasks[idx])
            func(idx + 1)
            subsets.pop()

        func(0)
        return self.ans


def generate_test_cases(num_cases=100, max_n=14, max_task_time=10, max_session_time=15):
    """Generate random test cases for the problem."""
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(1, max_n)  # Number of tasks
        tasks = [random.randint(1, max_task_time) for _ in range(n)]
        sessionTime = random.randint(max(max(tasks), 1), max_session_time)
        test_cases.append({"tasks": tasks, "sessionTime": sessionTime})
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the test cases."""
    solution = Solution()
    outputs = []
    for case in test_cases:
        tasks = case["tasks"]
        sessionTime = case["sessionTime"]
        output = solution.minSessions(tasks, sessionTime)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=50)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": case, "output": output} for case, output in zip(test_cases, expected_outputs)]

with open("test_cases_1986.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
