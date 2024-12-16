import json
import random
from typing import Optional, List


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0

        def dfs(node, left, right):
            self.maxi = max(self.maxi, left, right)

            if node.left:
                dfs(node.left, right + 1, 0)

            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.maxi


# Helper function to generate a random binary tree
def generate_random_tree(max_nodes=50_000):
    if max_nodes == 0:
        return None

    root = TreeNode(random.randint(1, 100))
    nodes = [root]
    for _ in range(max_nodes - 1):
        node = TreeNode(random.randint(1, 100))
        parent = random.choice(nodes)
        if parent.left is None:
            parent.left = node
        elif parent.right is None:
            parent.right = node
        else:
            continue
        nodes.append(node)
    return root


# Serialize the binary tree for saving in JSON
def serialize_tree(root):
    if not root:
        return None
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


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the number of nodes
        num_nodes = random.randint(1, 5000)
        # Generate a random binary tree
        root = generate_random_tree(num_nodes)
        # Compute the expected output using the solution
        expected_output = solution.longestZigZag(root)
        # Serialize the tree
        serialized_tree = serialize_tree(root)
        # Add the test case to the list
        test_cases.append({"input": serialized_tree, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1372.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 10 test cases
generate_test_cases()
