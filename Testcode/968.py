import json
import random
from typing import Optional, List, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            res = dfs(node.left) + dfs(node.right)
            curr = min(
                node.left.val if node.left else float('inf'),
                node.right.val if node.right else float('inf')
            )
            if curr == 0:
                node.val = 1
                res += 1
            elif curr == 1:
                node.val = 2
            return res

        return dfs(root) + (root.val == 0)


def generate_random_binary_tree(max_depth: int, probability=0.7) -> Optional[TreeNode]:
    """Generate a random binary tree with a specified max depth and node generation probability."""
    if max_depth == 0 or random.random() > probability:
        return None
    root = TreeNode(0)
    root.left = generate_random_binary_tree(max_depth - 1, probability)
    root.right = generate_random_binary_tree(max_depth - 1, probability)
    return root


def serialize_tree(root: Optional[TreeNode]) -> List[Union[int, None]]:
    """Serialize a binary tree to a list (level-order traversal)."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


def generate_test_cases(num_cases=50, max_depth=10):
    """Generate test cases for the Minimum Number of Cameras problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        root = generate_random_binary_tree(max_depth)
        if not root:
            serialized_tree = []  # Empty tree if root is None
            expected_output = 0
        else:
            serialized_tree = serialize_tree(root)
            expected_output = solution.minCameraCover(root)
        test_cases.append({"input": serialized_tree, "output": expected_output})

    # Add predefined edge cases

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_depth = 10
    test_cases = generate_test_cases(num_cases, max_depth)
    save_test_cases("test_cases_968.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'min_camera_cover_test_cases.json'.")
