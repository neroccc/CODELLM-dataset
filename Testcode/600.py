import json
import random

class Solution:
    def findIntegers(self, n: int) -> int:
        # f stores the fibonacci numbers
        f = [1, 2]
        for i in range(2, 31):
            f.append(f[-1] + f[-2])
        # last_seen tells us if there was a one right before.
        # If that is the case, we are done then and there!
        # ans is the answer
        ans, last_seen = 0, 0
        for i in reversed(range(31)):
            if (1 << i) & n: # is the ith bit set?
                ans += f[i]
                if last_seen:
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans + 1


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random n in the range [1, 10^9]
        n = random.randint(1, 10**9)
        # Compute the output using the solution's method
        output = solution.findIntegers(n)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_600.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
