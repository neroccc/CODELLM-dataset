import json
import random
import string


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, root, key):
        curr = root
        for i in range(len(key)):
            idx = ord(key[i]) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def dfs(self, root, key, index, count):
        if index >= len(key):
            return count > 1
        curr = root
        for i in range(index, len(key)):
            p = ord(key[i]) - ord('a')
            if not curr.children[p]:
                return False
            curr = curr.children[p]
            if curr.is_end:
                if self.dfs(root, key, i + 1, count + 1):
                    return True
        return False

    def findAllConcatenatedWordsInADict(self, words):
        for i in range(len(words)):
            self.insert(self.root, words[i])
        ans = []
        for i in range(len(words)):
            if self.dfs(self.root, words[i], 0, 0):
                ans.append(words[i])
        return ans


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    def random_word(length):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    for _ in range(num_cases):
        # Generate a random number of words
        num_words = random.randint(5, 50)
        words = [random_word(random.randint(1, 10)) for _ in range(num_words)]

        # Add some concatenated words
        for _ in range(random.randint(1, num_words // 2)):
            word1 = random.choice(words)
            word2 = random.choice(words)
            if word1 != word2:  # Avoid duplicates
                words.append(word1 + word2)

        # Shuffle the words to simulate realistic input
        random.shuffle(words)

        # Calculate expected output
        expected_output = solution.findAllConcatenatedWordsInADict(words)

        # Add test case
        test_cases.append({
            "input": {"words": words},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_472.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
