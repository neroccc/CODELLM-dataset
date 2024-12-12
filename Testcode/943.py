import json
import random
import string
from collections import defaultdict
from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def getMinSuffix(w1, w2):
            n = min(len(w1), len(w2))
            for i in range(n, 0, -1):
                if w1[-i:] == w2[:i]:
                    return w2[i:]
            return w2

        n = len(words)
        suffix = defaultdict(dict)
        for i in range(n):
            for j in range(n):
                suffix[i][j] = getMinSuffix(words[i], words[j])
        dp = [[''] * n for _ in range(1 << n)]
        for i in range(1, 1 << n):
            indexes = [j for j in range(n) if i & (1 << j)]
            for j in indexes:
                i2 = i & ~(1 << j)
                strs = [dp[i2][j2] + suffix[j2][j] for j2 in indexes if j2 != j]
                dp[i][j] = min(strs, key=len) if strs else words[j]
        return min(dp[-1], key=len)

def generate_random_word(max_length):
    """Generate a random word of a given maximum length."""
    length = random.randint(1, max_length)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_test_cases(num_cases=50, max_words=12, max_length=20):
    """Generate test cases for the Shortest Superstring problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        num_words = random.randint(1, max_words)
        words = [generate_random_word(max_length) for _ in range(num_words)]
        expected_output = solution.shortestSuperstring(words)
        test_cases.append({"input": words, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": ["alex", "loves", "leetcode"], "output": solution.shortestSuperstring(["alex", "loves", "leetcode"])},
        {"input": ["catg", "ctaagt", "gcta", "ttca", "atgcatc"], "output": solution.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])},
        {"input": ["a", "b", "c"], "output": solution.shortestSuperstring(["a", "b", "c"])},
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
    max_words = 12
    max_length = 20
    test_cases = generate_test_cases(num_cases, max_words, max_length)
    save_test_cases("test_cases_943.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'shortest_superstring_test_cases.json'.")
