from typing import List, Optional, Any
from deepseekcode.help.helphelp import TreeNode, serialize_tree  # Import TreeNode and serialize_tree from helphelp.py
from functools import lru_cache, cache


class Solution:
    def allPossibleFBT(self, n: int) -> List[List[Any]]:
        if n % 2 == 0:
            return []

        @cache
        def dfs(n: int) -> List[Optional[TreeNode]]:
            if n == 1:
                return [TreeNode(0)]

            ans = []
            for i in range(1, n, 2):
                left = dfs(i)
                right = dfs(n - i - 1)
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        ans.append(root)

            return ans

        all_trees = dfs(n)
        return [serialize_tree(tree) for tree in all_trees]