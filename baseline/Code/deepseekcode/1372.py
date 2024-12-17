from typing import List, Any
from deepseekcode.help.helphelp import TreeNode, deserialize_tree
class Solution:
    def longestZigZag(self, root: List[Any]) -> int:
        root = deserialize_tree(root)
        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return [-1, -1, -1]
            left, right = dfs(node.left), dfs(node.right)
            return [
                max(left[0], right[1]) + 1, # longest zig
                max(left[1], right[0]) + 1, # longest zag
                max(left) if node.left else -1, # max zig or zag of left child
                max(right) if node.right else -1, # max zig or zag of right child
            ]
        return max(dfs(root))