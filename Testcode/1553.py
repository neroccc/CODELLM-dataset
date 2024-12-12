import json
import random


class Solution:
    def minDays(self, n: int) -> int:
        ans = 0
        queue = [n]
        seen = set()
        while queue:  # BFS
            newq = []
            for x in queue:
                if x == 0:
                    return ans
                seen.add(x)
                if x - 1 not in seen:
                    newq.append(x - 1)
                if x % 2 == 0 and x // 2 not in seen:
                    newq.append(x // 2)
                if x % 3 == 0 and x // 3 not in seen:
                    newq.append(x // 3)
            ans += 1
            queue = newq


# Generate test cases
def generate_test_cases(num_cases=1000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomly generate values for n within the range [1, 2 * 10^9]
        n = random.randint(1, 2 * 10 ** 9)

        # Compute expected output using the provided solution
        expected_output = solution.minDays(n)

        test_cases.append({
            "input": {"n": n},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1553.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
