import json
import random
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}

        def _allPossibleFBT(n):
            if n in memo:
                return memo[n]

            trees = []
            if n == 1:
                trees.append(TreeNode(0))
            else:
                for i in range(1, n - 1, 2):
                    lTrees = _allPossibleFBT(i)
                    rTrees = _allPossibleFBT(n - i - 1)

                    for lt in lTrees:
                        for rt in rTrees:
                            trees.append(TreeNode(0, lt, rt))

            memo[n] = trees
            return trees

        return _allPossibleFBT(n)


def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serialize the binary tree into a list for easy comparison."""
    if not root:
        return []

    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for compactness
    while result and result[-1] is None:
        result.pop()

    return result


def generate_test_cases(num_cases=10):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        n = random.randint(1, 20)  # Ensure n is odd
        trees = solution.allPossibleFBT(n)
        serialized_trees = [serialize_tree(tree) for tree in trees]
        test_cases.append({
            "input": {
                "n": n
            },
            "output": serialized_trees
        })

    # Save to a JSON file
    with open("test_cases_894.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=10)
