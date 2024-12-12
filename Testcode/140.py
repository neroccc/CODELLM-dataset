import json
import random
import string
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Map to store results of subproblems
        dp = {}

        # Iterate from the end of the string to the beginning
        for start_idx in range(len(s), -1, -1):
            # List to store valid sentences starting from start_idx
            valid_sentences = []

            # Iterate from start_idx to the end of the string
            for end_idx in range(start_idx, len(s)):
                # Extract substring from start_idx to end_idx
                current_word = s[start_idx : end_idx + 1]

                # Check if the current substring is a valid word
                if self.is_word_in_dict(current_word, wordDict):
                    # If it's the last word, add it as a valid sentence
                    if end_idx == len(s) - 1:
                        valid_sentences.append(current_word)
                    else:
                        # If it's not the last word, append it to each sentence formed by the remaining substring
                        sentences_from_next_index = dp.get(end_idx + 1, [])
                        for sentence in sentences_from_next_index:
                            valid_sentences.append(
                                current_word + " " + sentence
                            )

            # Store the valid sentences in dp
            dp[start_idx] = valid_sentences

        # Return the sentences formed from the entire string
        return dp.get(0, [])

    # Helper function to check if a word is in the word dictionary
    def is_word_in_dict(self, word: str, word_dict: List[str]) -> bool:
        return word in word_dict

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

def save_test_cases_to_file(test_cases, filename="test_cases_140.json"):
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
