import json
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)

        for numberOfNodes in range(1, n + 1):
            for i in range(1, numberOfNodes + 1):
                j = numberOfNodes - i
                for left in dp[i - 1]:
                    for right in dp[j]:
                        root = TreeNode(i, left, self.clone(right, i))
                        dp[numberOfNodes].append(root)

        return dp[n]

    def clone(
        self, node: Optional[TreeNode], offset: int
    ) -> Optional[TreeNode]:
        if not node:
            return None
        cloned_node = TreeNode(node.val + offset)
        cloned_node.left = self.clone(node.left, offset)
        cloned_node.right = self.clone(node.right, offset)
        return cloned_node

def count_unique_bsts(n: int) -> int:
    """
    Utility function to count the number of unique BSTs for a given n.
    """
    solution = Solution()
    unique_trees = solution.generateTrees(n)
    return len(unique_trees)

def generate_test_cases(num_cases=8):
    """
    Generates test cases for the generateTrees function.

    :param num_cases: Number of test cases to generate (1 to 8).
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    for n in range(1, num_cases + 1):
        expected_output = count_unique_bsts(n)
        test_cases.append({
            "input": n,
            "output": expected_output
        })
    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_95.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    num_cases = 8
    test_cases = generate_test_cases(num_cases=num_cases)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
