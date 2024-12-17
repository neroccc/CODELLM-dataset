from typing import List, Any
from deepseekcode.help.helphelp import TreeNode, serialize_tree,deserialize_tree  # Import from helphelp.py

class Solution:
    def allPossibleFBT(self, n: int) -> List[List[Any]]:
        """
        Generates all possible full binary trees with n nodes and returns them serialized as level-order lists.
        :param n: Number of nodes in the full binary tree (must be odd).
        :return: List of serialized level-order representations of full binary trees.
        """
        # Full Binary Trees only exist with odd n
        if n % 2 == 0:
            return []
        if n == 1:
            return [serialize_tree(TreeNode(0))]  # A single node tree serialized

        res = []
        # Generate all possible left and right subtrees
        for i in range(1, n, 2):  # Only odd numbers for left subtree size
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(n - i - 1)

            # Connect left and right subtrees to a new root
            for left in lefts:
                for right in rights:
                    root = TreeNode(0)
                    root.left = deserialize_tree(left)  # Deserialize for TreeNode structure
                    root.right = deserialize_tree(right)
                    res.append(serialize_tree(root))  # Serialize the new full binary tree

        return res
