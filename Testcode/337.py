import json
import random
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob_saved = {}
        not_rob_saved = {}

        def helper(node, parent_robbed):
            if not node:
                return 0

            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result = helper(node.left, False) + helper(node.right, False)
                rob_saved[node] = result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob = node.val + helper(node.left, True) + helper(node.right, True)
                not_rob = helper(node.left, False) + helper(node.right, False)
                result = max(rob, not_rob)
                not_rob_saved[node] = result
                return result

        return helper(root, False)

def generate_random_tree(max_nodes=10**4, max_value=10**4) -> Optional[TreeNode]:
    """
    Generates a random binary tree with up to max_nodes nodes.

    :param max_nodes: Maximum number of nodes in the tree.
    :param max_value: Maximum value for the node values.
    :return: Root of the randomly generated binary tree.
    """
    if max_nodes == 0:
        return None

    def add_children(node, remaining_nodes):
        if remaining_nodes == 0:
            return 0

        nodes_created = 0
        if random.choice([True, False]) and remaining_nodes > 0:
            node.left = TreeNode(random.randint(0, max_value))
            nodes_created += 1
            nodes_created += add_children(node.left, remaining_nodes - nodes_created)
        if random.choice([True, False]) and remaining_nodes > 0:
            node.right = TreeNode(random.randint(0, max_value))
            nodes_created += 1
            nodes_created += add_children(node.right, remaining_nodes - nodes_created)

        return nodes_created

    root = TreeNode(random.randint(0, max_value))
    add_children(root, max_nodes - 1)
    return root

def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Serializes a binary tree into a list format.

    :param root: Root of the binary tree.
    :return: List representing the serialized binary tree.
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

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result

def generate_test_cases(num_cases=100, max_nodes=50, max_value=100):
    """
    Generates test cases for the rob function.

    :param num_cases: Number of test cases to generate.
    :param max_nodes: Maximum number of nodes in each tree.
    :param max_value: Maximum value for the node values.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Generate a random binary tree
        root = generate_random_tree(max_nodes=max_nodes, max_value=max_value)

        # Calculate the expected output using the provided solution
        expected_output = solution.rob(root)

        # Add test case
        test_cases.append({
            "input": serialize_tree(root),
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_337.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_nodes=10, max_value=50)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
