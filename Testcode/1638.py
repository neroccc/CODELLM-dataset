import json
import random
import string

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        equal_prev, unequal_prev = [0] * (lt + 1), [0] * (lt + 1)
        ans = 0
        for i in range(ls):
            equal_curr, unequal_curr = [0] * (lt + 1), [0] * (lt + 1)
            for j in range(lt):
                if s[i] == t[j]:
                    equal_curr[j + 1] = 1 + equal_prev[j]
                unequal_curr[j + 1] = 1 + equal_prev[j] if s[i] != t[j] else unequal_prev[j]
                ans += unequal_curr[j + 1]
            equal_prev, unequal_prev = equal_curr, unequal_curr
        return ans

# Helper function to generate random strings
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        len_s = random.randint(1, 100)
        len_t = random.randint(1, 100)
        s = generate_random_string(len_s)
        t = generate_random_string(len_t)
        expected_output = solution.countSubstrings(s, t)

        test_cases.append({
            "input": {"s": s, "t": t},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1638.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
