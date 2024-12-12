import json
import random


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n, end = len(s), minJump
        reach = [True] + [False] * (n - 1)
        for i in range(n):
            if reach[i]:
                start, end = max(i + minJump, end), min(i + maxJump + 1, n)
                for j in range(start, end):
                    if s[j] == '0':
                        reach[j] = True
                if end == n:
                    return reach[-1]
        return reach[-1]


# Generate random test cases
def generate_test_cases(num_cases=50, max_len=1000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(2, max_len)
        min_jump = random.randint(1, length - 1)
        max_jump = random.randint(min_jump, length - 1)

        # Generate a random binary string with '0' and '1'
        s = "0" + ''.join(random.choice("01") for _ in range(length - 2)) + "0"

        expected_output = solution.canReach(s, min_jump, max_jump)

        test_cases.append({
            "input": {"s": s, "minJump": min_jump, "maxJump": max_jump},
            "output": expected_output
        })

    # Save to a file
    with open("test_cases_1871.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
