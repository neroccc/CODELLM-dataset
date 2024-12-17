from typing import List, Any
from deepseekcode.help.helphelp import TreeNode, serialize_tree  # Import TreeNode and serialize_tree from helphelp.py


class Solution:
    def generateTrees(self, n: int) -> List[List[Any]]:
        """
        Generates all unique BSTs for values 1 to n and returns them serialized as level-order lists.
        :param n: Number of nodes in the BST.
        :return: List of serialized trees in level-order format.
        """

        # Helper function to generate unique BSTs
        def generate_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):  # Pick i as the root
                left_trees = generate_trees(start, i - 1)  # Left subtrees
                right_trees = generate_trees(i + 1, end)  # Right subtrees

                # Connect all combinations of left and right subtrees to root
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        # Generate all unique BSTs
        all_trees = generate_trees(1, n) if n else []

        # Serialize all generated trees using helphelp's serialize_tree
        return [serialize_tree(tree) for tree in all_trees]
