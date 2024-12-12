import json
import random
from typing import List
from collections import Counter
import copy


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersCounter = Counter(letters)
        totalScore = 0

        def explore(index, letterCounter, currScore):
            nonlocal totalScore

            totalScore = max(totalScore, currScore)
            if index == len(words):
                return

            for i in range(index, len(words)):
                tmpCounter = copy.deepcopy(letterCounter)
                word = words[i]
                wordScore = 0
                isValid = True

                for ch in word:
                    if ch in tmpCounter and tmpCounter[ch] > 0:
                        tmpCounter[ch] -= 1
                        wordScore += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
                if isValid:
                    explore(i + 1, tmpCounter, currScore + wordScore)

        explore(0, lettersCounter, 0)
        return totalScore


def generate_random_words(max_words=14, max_word_length=15):
    """Generate a random list of words."""
    num_words = random.randint(1, max_words)
    words = []
    for _ in range(num_words):
        word_length = random.randint(1, max_word_length)
        word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=word_length))
        words.append(word)
    return words


def generate_random_letters(max_letters=100):
    """Generate a random list of letters."""
    num_letters = random.randint(1, max_letters)
    return random.choices('abcdefghijklmnopqrstuvwxyz', k=num_letters)


def generate_random_score():
    """Generate a random score array for letters."""
    return [random.randint(0, 10) for _ in range(26)]


def generate_test_cases(num_cases=50):
    """Generate test cases for the Maximum Score of Words Formed by Letters problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        words = generate_random_words()
        letters = generate_random_letters()
        score = generate_random_score()
        expected_output = solution.maxScoreWords(words, letters, score)
        test_cases.append({"input": {"words": words, "letters": letters, "score": score}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {
            "input": {
                "words": ["dog", "cat", "dad", "good"],
                "letters": ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                "score": [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            },
            "output": solution.maxScoreWords(
                ["dog", "cat", "dad", "good"],
                ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ),
        },
        {
            "input": {
                "words": ["xxxz", "ax", "bx", "cx"],
                "letters": ["z", "a", "b", "c", "x", "x", "x"],
                "score": [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10],
            },
            "output": solution.maxScoreWords(
                ["xxxz", "ax", "bx", "cx"],
                ["z", "a", "b", "c", "x", "x", "x"],
                [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10],
            ),
        },
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
    test_cases = generate_test_cases(num_cases)
    save_test_cases("../test_cases_1255.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'max_score_words_test_cases.json'.")
