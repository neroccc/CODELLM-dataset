import json
import random

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        GOOD, BAD, UNKNOWN = 1, 0, -1
        memo = [UNKNOWN] * len(nums)
        memo[-1] = GOOD
        for i in range(len(nums) - 2, -1, -1):
            furthest_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest_jump + 1):
                if memo[j] == GOOD:
                    memo[i] = GOOD
                    break
        return memo[0] == GOOD

def generate_test_cases(num_cases=1000, max_length=100, max_value=10**5):
    """
    Generates test cases for the canJump function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the array.
    :param max_value: Maximum value of the elements in the array.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate a random array with varying lengths and values
        length = random.randint(2, max_length)
        nums = [random.randint(0, max_value) for _ in range(length)]

        # Calculate the expected output using the provided solution
        expected_output = solution.canJump(nums)

        # Add test case
        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_55.json"):
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
    test_cases = generate_test_cases(num_cases=num_cases, max_length=100, max_value=10**5)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
