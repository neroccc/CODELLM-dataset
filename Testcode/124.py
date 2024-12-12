import json
import random
from typing import Optional, List, Any

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float("inf")

        def gainFromSubtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath
            if not node:
                return 0
            gainFromLeft = max(gainFromSubtree(node.left), 0)
            gainFromRight = max(gainFromSubtree(node.right), 0)
            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)
            return max(gainFromLeft + node.val, gainFromRight + node.val)

        gainFromSubtree(root)
        return maxPath

def generate_random_tree(depth=5, max_val=1000):
    """
    Generates a random binary tree.

    :param depth: Maximum depth of the tree.
    :param max_val: Maximum absolute value of node values.
    :return: Root node of the generated binary tree.
    """
    if depth == 0 or random.random() > 0.7:
        return None

    root = TreeNode(val=random.randint(-max_val, max_val))
    root.left = generate_random_tree(depth - 1, max_val)
    root.right = generate_random_tree(depth - 1, max_val)
    return root

def serialize_tree(root: Optional[TreeNode]) -> List[Any]:
    """
    Serializes a binary tree into a list.

    :param root: Root of the binary tree.
    :return: Serialized list representation of the binary tree.
    """
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

    while result and result[-1] is None:
        result.pop()

    return result

def generate_test_cases(num_cases=100, max_depth=5, max_val=1000):
    """
    Generates test cases for the maxPathSum function.

    :param num_cases: Number of test cases to generate.
    :param max_depth: Maximum depth of the binary trees.
    :param max_val: Maximum absolute value of node values.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        root = generate_random_tree(max_depth, max_val)
        serialized_tree = serialize_tree(root)
        expected_output = solution.maxPathSum(root)
        test_cases.append({
            "input": serialized_tree,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_124.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_depth=5, max_val=1000)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
