import json
import random
import string


class Solution:
    def minimumDistance(self, word: str) -> int:
        col = 6

        def ord_to_cor(cor: int):
            return (cor // col, cor % col)

        def distance(curr: str, target: str):
            if curr == ".": return 0
            cor_curr = ord_to_cor(ord(curr) - ord("A"))
            cor_target = ord_to_cor(ord(target) - ord("A"))
            return abs(cor_curr[0] - cor_target[0]) + abs(cor_curr[1] - cor_target[1])

        memo = {}

        def dfs(i: int, first: str, second: str) -> int:
            if i == len(word): return 0
            if (i, first, second) in memo: return memo[(i, first, second)]

            memo[(i, first, second)] = min(
                distance(first, word[i]) + dfs(i + 1, word[i], second),
                distance(second, word[i]) + dfs(i + 1, first, word[i])
            )
            return memo[(i, first, second)]

        return dfs(0, ".", ".")


# Generate diverse test cases
def generate_test_cases(num_cases=1000):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the length of the word
        length = random.randint(2, 300)
        # Generate a random word of the decided length
        word = ''.join(random.choices(string.ascii_uppercase, k=length))
        # Compute the expected output using the solution
        expected_output = solution.minimumDistance(word)
        # Add the test case to the list
        test_cases.append({"input": word, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1320.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 1000 test cases
generate_test_cases()
