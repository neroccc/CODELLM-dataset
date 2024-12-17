from typing import List, Any, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generate_trees(self, n: int) -> List[List[Any]]:
        # Helper function to generate unique BSTs
        def generate_trees_helper(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees_helper(start, i - 1)
                right_trees = generate_trees_helper(i + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(i)
                        root.left = left_tree
                        root.right = right_tree
                        all_trees.append(root)

            return all_trees

        # Serialize a tree to a level-order list
        def serialize_tree(root: Optional[TreeNode]) -> List[Any]:
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

        # Generate all trees and serialize them
        all_trees = generate_trees_helper(1, n)
        return [serialize_tree(tree) for tree in all_trees]

    # Deserialization function for later use
    def deserialize_tree(self, data: List[Any]) -> Optional[TreeNode]:
        if not data:
            return None

        root = TreeNode(data[0])
        queue = [root]
        index = 1

        while queue and index < len(data):
            node = queue.pop(0)

            if data[index] is not None:
                node.left = TreeNode(data[index])
                queue.append(node.left)
            index += 1

            if index < len(data) and data[index] is not None:
                node.right = TreeNode(data[index])
                queue.append(node.right)
            index += 1

        return root