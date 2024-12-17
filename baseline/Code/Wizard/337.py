from typing import Optional, List, Any
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: List[Any]) -> int:
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
        def helper(node):
            if not node:
                return [0, 0]

            left = helper(node.left)
            right = helper(node.right)

            return [node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])]

        return max(helper(root))