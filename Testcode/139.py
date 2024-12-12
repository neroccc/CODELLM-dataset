import json
import random
import string
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]

def generate_random_string(length: int) -> str:
    """
    Generates a random lowercase English string.

    :param length: Length of the string to generate.
    :return: Random string of the specified length.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_word_dict(max_words: int, max_word_length: int) -> List[str]:
    """
    Generates a random list of words for the dictionary.

    :param max_words: Maximum number of words in the dictionary.
    :param max_word_length: Maximum length of each word.
    :return: List of random words.
    """
    return [generate_random_string(random.randint(1, max_word_length)) for _ in range(random.randint(1, max_words))]

def generate_test_cases(num_cases=100, max_s_length=20, max_words=10, max_word_length=10):
    """
    Generates test cases for the wordBreak function.

    :param num_cases: Number of test cases to generate.
    :param max_s_length: Maximum length of the string `s`.
    :param max_words: Maximum number of words in the dictionary.
    :param max_word_length: Maximum length of each word in the dictionary.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate random string `s`
        s_length = random.randint(1, max_s_length)
        s = generate_random_string(s_length)

        # Generate random word dictionary
        wordDict = generate_word_dict(max_words, max_word_length)

        # Calculate the expected output using the provided solution
        expected_output = solution.wordBreak(s, wordDict)

        # Add test case
        test_cases.append({
            "input": {"s": s, "wordDict": wordDict},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_139.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_s_length=20, max_words=10, max_word_length=10)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
