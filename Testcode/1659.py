import json
import random
from functools import cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:

        @cache
        def fn(prev, i, j, intro, extro):
            if i == m:
                return 0  # No more positions
            if j == n:
                return fn(prev, i + 1, 0, intro, extro)
            if intro == extro == 0:
                return 0

            prev0 = prev[:j] + (0,) + prev[j + 1:]
            ans = fn(prev0, i, j + 1, intro, extro)
            if intro:
                val = 120
                if i and prev[j]:
                    val -= 30
                    if prev[j] == 1:
                        val -= 30
                    else:
                        val += 20
                if j and prev[j - 1]:
                    val -= 30
                    if prev[j - 1] == 1:
                        val -= 30
                    else:
                        val += 20
                prev0 = prev[:j] + (1,) + prev[j + 1:]
                ans = max(ans, val + fn(prev0, i, j + 1, intro - 1, extro))
            if extro:
                val = 40
                if i and prev[j]:
                    val += 20
                    if prev[j] == 1:
                        val -= 30
                    else:
                        val += 20
                if j and prev[j - 1]:
                    val += 20
                    if prev[j - 1] == 1:
                        val -= 30
                    else:
                        val += 20
                prev0 = prev[:j] + (2,) + prev[j + 1:]
                ans = max(ans, val + fn(prev0, i, j + 1, intro, extro - 1))
            return ans

        return fn((0,) * n, 0, 0, introvertsCount, extrovertsCount)


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        m = random.randint(1, 5)
        n = random.randint(1, 5)
        max_people = min(m * n, 6)
        introvertsCount = random.randint(0, max_people)
        extrovertsCount = random.randint(0, max_people - introvertsCount)

        expected_output = solution.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount)

        test_cases.append({
            "input": {"m": m, "n": n, "introvertsCount": introvertsCount, "extrovertsCount": extrovertsCount},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1659.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
