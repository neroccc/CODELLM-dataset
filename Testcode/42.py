import json
import random

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans

def generate_test_cases(num_cases=1000, max_length=100, max_height=100):
    """
    Generates test cases for the trap function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the elevation map.
    :param max_height: Maximum height of each bar in the elevation map.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, max_length)
        height = [random.randint(0, max_height) for _ in range(length)]
        expected_output = solution.trap(height)
        test_cases.append({
            "input": height,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_42.json"):
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
    test_cases = generate_test_cases(num_cases=num_cases, max_length=100, max_height=100)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
