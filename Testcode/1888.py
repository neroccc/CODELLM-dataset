import json
import random

def generate_test_cases(num_cases=1000):
    test_cases = []
    for _ in range(num_cases):
        # Generate a random binary string of varying lengths
        length = random.randint(1, 100)  # Adjust upper limit for practical purposes
        binary_string = ''.join(random.choice(['0', '1']) for _ in range(length))
        test_cases.append(binary_string)
    return test_cases

def compute_expected_outputs(test_cases):
    solution = Solution()  # Ensure to use the provided solution
    outputs = []
    for case in test_cases:
        output = solution.minFlips(case)
        outputs.append(output)
    return outputs

class Solution:
    def minFlips(self, s: str) -> int:
        import sys
        prev = 0
        start_1, start_0, start_1_odd, start_0_odd = 0, 0, sys.maxsize, sys.maxsize
        odd = len(s) % 2
        for val in s:
            val = int(val)
            if val == prev:
                if odd:
                    start_0_odd = min(start_0_odd, start_1)
                    start_1_odd += 1
                start_1 += 1
            else:
                if odd:
                    start_1_odd = min(start_1_odd, start_0)
                    start_0_odd += 1
                start_0 += 1
            prev = 1 - prev
        return min([start_1, start_0, start_1_odd, start_0_odd])

# Generate test cases
test_cases = generate_test_cases()

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": case, "output": output} for case, output in zip(test_cases, expected_outputs)]

with open("test_cases_1888.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
