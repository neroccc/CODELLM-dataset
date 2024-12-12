import random
import string
import json


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        ans = [0, 0]
        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i: j + 1]


def generate_random_string(length, chars=string.ascii_letters + string.digits):
    """Generates a random string of given length using specified characters."""
    return ''.join(random.choice(chars) for _ in range(length))


def generate_test_cases(num_cases, min_length=1, max_length=1000):
    """Generates test cases for the longest palindrome problem."""
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Generate a random string
        length = random.randint(min_length, max_length)
        test_input = generate_random_string(length)

        # Compute the expected output using the correct solution
        expected_output = solution.longestPalindrome(test_input)

        # Add the test case to the list
        test_cases.append({"input": test_input, "output": expected_output})

    return test_cases


def main():
    # Number of test cases to generate
    num_cases = 1000

    # Generate test cases
    test_cases = generate_test_cases(num_cases)

    # Save the test cases to a JSON file
    with open("../test_cases_5.json", "w") as f:
        json.dump(test_cases, f, indent=4)

    print(f"{num_cases} test cases have been saved to 'test_cases.json'.")


if __name__ == "__main__":
    main()
