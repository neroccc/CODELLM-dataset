import json
import random
import string

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [
            [None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]

        def minDistanceRecur(word1, word2, word1Index, word2Index):
            if word1Index == 0:
                return word2Index
            if word2Index == 0:
                return word1Index
            if memo[word1Index][word2Index] is not None:
                return memo[word1Index][word2Index]
            minEditDistance = 0
            if word1[word1Index - 1] == word2[word2Index - 1]:
                minEditDistance = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
            else:
                insertOperation = minDistanceRecur(
                    word1, word2, word1Index, word2Index - 1
                )
                deleteOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index
                )
                replaceOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
                minEditDistance = (
                    min(insertOperation, deleteOperation, replaceOperation) + 1
                )
            memo[word1Index][word2Index] = minEditDistance
            return minEditDistance

        return minDistanceRecur(word1, word2, len(word1), len(word2))

def generate_test_cases(num_cases=1000, max_length=100):
    """
    Generates test cases for the minDistance function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the words.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate random lengths for word1 and word2
        len_word1 = random.randint(0, max_length)
        len_word2 = random.randint(0, max_length)

        # Generate random words
        word1 = ''.join(random.choices(string.ascii_lowercase, k=len_word1))
        word2 = ''.join(random.choices(string.ascii_lowercase, k=len_word2))

        # Calculate the expected output using the provided solution
        expected_output = solution.minDistance(word1, word2)

        # Add test case
        test_cases.append({
            "input": {"word1": word1, "word2": word2},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_72.json"):
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
    test_cases = generate_test_cases(num_cases=num_cases, max_length=100)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
