import json
import random
import string
from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_chain = 0
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            max_chain = max(max_chain, dp[word])
        return max_chain


def generate_random_word(min_length=1, max_length=16):
    """Generate a random word of length between min_length and max_length."""
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_random_word_list(min_length=1, max_length=16, max_words=1000):
    """Generate a list of random words."""
    num_words = random.randint(1, max_words)
    return [generate_random_word(min_length, max_length) for _ in range(num_words)]


def generate_test_cases(num_cases=50, max_words=1000, max_word_length=16):
    """Generate test cases for the Longest String Chain problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        words = generate_random_word_list(1, max_word_length, max_words)
        expected_output = solution.longestStrChain(words)
        test_cases.append({
            "input": words,
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": ["a", "b", "ba", "bca", "bda", "bdca"], "output": solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])},
        {"input": ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], "output": solution.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])},
        {"input": ["abcd", "dbqca"], "output": solution.longestStrChain(["abcd", "dbqca"])},
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
    max_words = 1000
    max_word_length = 16
    test_cases = generate_test_cases(num_cases, max_words, max_word_length)
    save_test_cases("../test_cases_1048.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'longest_string_chain_test_cases.json'.")
