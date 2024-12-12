import json
import random

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_subarray = max_subarray = nums[0]

        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray

def generate_test_cases(num_cases=1000, max_length=100, min_value=-10**4, max_value=10**4):
    """
    Generates test cases for the maxSubArray function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the array.
    :param min_value: Minimum value for array elements.
    :param max_value: Maximum value for array elements.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate a random array with varying lengths and values
        length = random.randint(1, max_length)
        nums = [random.randint(min_value, max_value) for _ in range(length)]

        # Calculate the expected output using the provided solution
        expected_output = solution.maxSubArray(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_53.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    num_cases = 1000
    test_cases = generate_test_cases(num_cases=num_cases, max_length=100, min_value=-10**4, max_value=10**4)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
