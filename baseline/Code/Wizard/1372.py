from typing import List,Any,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: List[Any]) -> int:
        """
        Calculates the maximum amount that can be robbed from a binary tree represented in serialized format.
        :param serialized_tree: List representing the tree in level-order traversal.
        :return: Maximum amount that can be robbed.
        """
        # Deserialize the tree
        def deserialize_tree(data: List[Any]) -> Optional[TreeNode]:
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

        root = deserialize_tree(root)
        def dfs(node, depth, direction):
            if not node:
                return depth - 1

            left_depth = dfs(node.left, depth + 1, 0)
            right_depth = dfs(node.right, depth + 1, 1)

            if direction == 0:
                return max(left_depth, right_depth)
            else:
                return max(right_depth, left_depth)

        return max(dfs(root, 0, 0), dfs(root, 0, 1))