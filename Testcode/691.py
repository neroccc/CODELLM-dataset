import collections
import json
import random
import string
from typing import List
from collections import Counter


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        result = self.dfs(stickers, target, 0, {})
        return result if result != float("inf") else -1

    def dfs(self, stickers, target, idx, memo):
        # if target is empty then we don't need to take any sticker
        if target == "":
            return 0
        # if we've searched through all stickers and haven't completed the target
        # then there is no solution
        if idx == len(stickers):
            return float("inf")

        # lookup the answer in the cache
        key = (idx, target)
        if key in memo:
            return memo[key]

        # choice 1 don't take the current sticker
        result = self.dfs(stickers, target, idx + 1, memo)

        # choice 2 try to take the current sticker
        currentSticker = stickers[idx]
        newTarget = target
        somethingRemoved = False
        for c in currentSticker:
            idxToRemove = newTarget.find(c)
            if idxToRemove != -1:
                newTarget = newTarget[:idxToRemove] + newTarget[idxToRemove + 1:]
                somethingRemoved = True

        # only try this sticker again if we were able to remove something from
        # the target string
        if somethingRemoved:
            result = min(result, 1 + self.dfs(stickers, newTarget, idx, memo))

        # cache the result
        memo[key] = result
        return result


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate random number of stickers (1 to 50)
        n = random.randint(1, 50)
        # Generate random stickers with lengths between 1 and 10
        stickers = [
            ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 10)))
            for _ in range(n)
        ]
        # Generate a random target with length between 1 and 15
        target = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 15)))
        # Compute the output using the solution's method
        output = solution.minStickers(stickers, target)
        # Append the test case
        test_cases.append({
            "input": {
                "stickers": stickers,
                "target": target
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_691.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
