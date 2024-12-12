import json
import random
import string


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            prev = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1
                prev = temp
        return dp[n - 1]


# Generate diverse test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the length of the string
        length = random.randint(1, 500)
        # Generate a random string of the decided length
        s = ''.join(random.choices(string.ascii_lowercase, k=length))
        # Compute the expected output using the solution
        expected_output = solution.minInsertions(s)
        # Add the test case to the list
        test_cases.append({"input": s, "output": expected_output})

    # Save the test cases to a file
    with open("../test_cases_1312.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 1000 test cases
generate_test_cases()
