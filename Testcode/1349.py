import json
import random
from typing import List
import collections


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [collections.defaultdict(int) for _ in range(m + 1)]
        dp[-1][0] = 0

        bits = []
        for row in seats:
            num = 0
            for i in range(n):
                num += (row[i] == '.') << n - 1 - i
            bits.append(num)

        for i in range(m):
            for x in range(2 ** n):
                for y in dp[i - 1]:
                    if (
                            x & (x >> 1) == 0
                            and x & bits[i] == x
                            and x & (y >> 1) == 0
                            and (x >> 1) & y == 0
                    ):
                        dp[i][x] = max(dp[i][x], dp[i - 1][y] + bin(x).count('1'))

        return max(dp[m - 1][x] for x in dp[m - 1])


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the dimensions of the seat matrix
        m = random.randint(1, 8)
        n = random.randint(1, 8)
        # Generate a random seat matrix
        seats = [[random.choice(['#', '.']) for _ in range(n)] for _ in range(m)]
        # Compute the expected output using the solution
        expected_output = solution.maxStudents(seats)
        # Add the test case to the list
        test_cases.append({"input": seats, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1349.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 1000 test cases
generate_test_cases()
