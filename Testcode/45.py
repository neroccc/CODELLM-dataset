import json
import random

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                answer += 1
                cur_end = cur_far

        return answer

def generate_test_cases(num_cases=1000, max_length=100, max_value=1000):
    """
    Generates test cases for the jump function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the array.
    :param max_value: Maximum value of the elements in the array.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate a random array with a guaranteed path to the last index
        length = random.randint(2, max_length)  # Ensure at least 2 elements
        nums = [random.randint(1, max_value) for _ in range(length)]

        # Ensure it's possible to reach the last index
        for i in range(length - 2, -1, -1):
            nums[i] = max(nums[i], length - i - 1)

        expected_output = solution.jump(nums)

        test_cases.append({
            "input": nums,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_45.json"):
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
    test_cases = generate_test_cases(num_cases=num_cases, max_length=100, max_value=1000)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
