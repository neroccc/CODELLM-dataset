from deepseekcode.help.helphelp import TreeNode, deserialize_tree  # Import from helphelp.py
from typing import List, Any


class Solution:
    def rob(self, root: List[Any]) -> int:
        """
        Calculates the maximum amount that can be robbed from a binary tree provided in serialized format.
        :param serialized_tree: List representing the binary tree in level-order traversal.
        :return: Maximum amount that can be robbed.
        """
        # Deserialize the serialized tree into a TreeNode structure
        root = deserialize_tree(root)

        # Recursive helper function to compute the rob and not_rob values
        def helper(node: TreeNode) -> List[int]:
            if not node:
                return [0, 0]  # Base case: [not_rob, rob]

            # Recursively compute results for left and right subtrees
            left = helper(node.left)
            right = helper(node.right)

            # rob = current node's value + not_rob of left + not_rob of right
            rob = node.val + left[0] + right[0]

            # not_rob = maximum value we can get from left and right subtrees
            not_rob = max(left) + max(right)

            return [not_rob, rob]

        # Return the maximum of rob and not_rob for the root
        return max(helper(root))
