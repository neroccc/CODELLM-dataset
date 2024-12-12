import json
import random
import string
from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        lps = [0]
        k = 0
        for i in range(1, len(evil)):
            while k and evil[k] != evil[i]: k = lps[k - 1]
            if evil[k] == evil[i]: k += 1
            lps.append(k)

        @lru_cache(None)
        def fn(i, k, lower, upper):
            """Return number of good strings at position i and k prefix match."""
            if k == len(evil):
                return 0  # boundary condition
            if i == n:
                return 1
            lo = ord(s1[i]) - ord('a') if lower else 0
            hi = ord(s2[i]) - ord('a') if upper else 25

            ans = 0
            for x in range(lo, hi + 1):
                kk = k
                while kk and evil[kk] != chr(x + ord('a')):
                    kk = lps[kk - 1]
                if evil[kk] == chr(x + ord('a')):
                    kk += 1
                ans += fn(i + 1, kk, lower and x == lo, upper and x == hi)
            return ans

        return fn(0, 0, True, True) % 1_000_000_007


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the size of `n`
        n = random.randint(1, 500)
        # Generate random `s1` and `s2` of length `n`
        s1 = ''.join(random.choices(string.ascii_lowercase, k=n))
        s2 = ''.join(random.choices(string.ascii_lowercase, k=n))
        # Ensure s1 <= s2
        if s1 > s2:
            s1, s2 = s2, s1
        # Generate a random `evil` string of length up to 50
        evil_length = random.randint(1, min(50, n))
        evil = ''.join(random.choices(string.ascii_lowercase, k=evil_length))
        # Compute the expected output using the solution
        expected_output = solution.findGoodStrings(n, s1, s2, evil)
        # Add the test case to the list
        test_cases.append({"n": n, "s1": s1, "s2": s2, "evil": evil, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1397.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 10 test cases
generate_test_cases()
