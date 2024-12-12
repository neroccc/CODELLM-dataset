import json
import random
import string


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[9999] * 110 for _ in range(110)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, del_ = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1

                    if j - del_ >= 0:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1 + (
                            3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0))

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]


# Helper function to generate random strings
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 100)
        s = generate_random_string(length)
        k = random.randint(0, length)

        # Compute expected output using the provided solution
        expected_output = solution.getLengthOfOptimalCompression(s, k)

        test_cases.append({
            "input": {"s": s, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1531.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
