from typing import Optional, List, Any
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def maxPathSum(self, root: List[Any]) -> int:

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

        # Calculate max path sum
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum