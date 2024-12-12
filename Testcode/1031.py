import json
import random
from typing import List
from itertools import accumulate

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        nums = list(accumulate(nums, initial=0))
        mx1 = mx2 = mx3 = 0

        for sm0, sm1, sm2, sm3 in zip(nums,
                                      nums[firstLen:],
                                      nums[secondLen:],
                                      nums[firstLen + secondLen:]):
            mx1 = max(mx1, sm1 - sm0)
            mx2 = max(mx2, sm2 - sm0)
            mx3 = max(mx3, max(mx1 + sm3 - sm1, mx2 + sm3 - sm2))

        return mx3


def generate_random_array(min_length=2, max_length=1000, max_value=1000):
    """Generate a random array of integers."""
    length = random.randint(min_length, max_length)
    return [random.randint(0, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=1000, max_value=1000):
    """Generate test cases for the Maximum Sum of Two Non-Overlapping Subarrays problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(2, max_length)  # Ensure length >= 2
        nums = generate_random_array(length, max_length, max_value)

        # Ensure firstLen and secondLen are valid
        firstLen = random.randint(1, length // 2)
        secondLen = random.randint(1, length - firstLen)

        expected_output = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
        test_cases.append({
            "input": {
                "nums": nums,
                "firstLen": firstLen,
                "secondLen": secondLen
            },
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"nums": [0, 6, 5, 2, 2, 5, 1, 9, 4], "firstLen": 1, "secondLen": 2},
         "output": solution.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2)},
        {"input": {"nums": [3, 8, 1, 3, 2, 1, 8, 9, 0], "firstLen": 3, "secondLen": 2},
         "output": solution.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2)},
        {"input": {"nums": [2, 1, 5, 6, 0, 9, 5, 0, 3, 8], "firstLen": 4, "secondLen": 3},
         "output": solution.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3)},
        {"input": {"nums": [1, 2], "firstLen": 1, "secondLen": 1},
         "output": solution.maxSumTwoNoOverlap([1, 2], 1, 1)},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_length = 1000
    max_value = 1000
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("../test_cases_1031.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'max_sum_two_no_overlap_test_cases.json'.")
