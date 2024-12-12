from typing import List
import functools
import itertools


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))

        @functools.lru_cache(None)
        def get_min_largest_split_sum(curr_index: int, subarray_count: int):
            # Base Case: If there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. So return the sum of the remaining numbers.
            if subarray_count == 1:
                return prefix_sum[n] - prefix_sum[curr_index]

            # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining.
            minimum_largest_split_sum = prefix_sum[n]
            for i in range(curr_index, n - subarray_count + 1):
                # Store the sum of the first subarray.
                first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                # Find the maximum subarray sum for the current first split.
                largest_split_sum = max(first_split_sum,
                                        get_min_largest_split_sum(i + 1, subarray_count - 1))

                # Find the minimum among all possible combinations.
                minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                if first_split_sum >= minimum_largest_split_sum:
                    break

            return minimum_largest_split_sum

        return get_min_largest_split_sum(0, k)
import json
import random

def generate_test_cases(num_cases=100, max_nums_length=50, max_num_value=100, max_k=10):
    """
    Generates test cases for the splitArray function.

    :param num_cases: Number of test cases to generate.
    :param max_nums_length: Maximum length of the nums array.
    :param max_num_value: Maximum value for elements in nums.
    :param max_k: Maximum value for k.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        nums_length = random.randint(1, max_nums_length)
        nums = [random.randint(0, max_num_value) for _ in range(nums_length)]
        k = random.randint(1, min(max_k, nums_length))

        # Calculate the expected output using the provided solution
        expected_output = solution.splitArray(nums, k)

        # Add test case
        test_cases.append({
            "input": {"nums": nums, "k": k},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_410.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_nums_length=20, max_num_value=100, max_k=5)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
