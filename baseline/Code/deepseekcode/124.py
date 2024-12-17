from deepseekcode.help.helphelp import TreeNode, deserialize_tree  # Import from helphelp.py
from typing import List, Any
class Solution:
    def maxPathSum(self, root: List[Any]) -> int:
        root = deserialize_tree(root)
        def max_gain(node: TreeNode) -> int:
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            max_sum = max(max_sum, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum