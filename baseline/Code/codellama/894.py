from typing import List
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n == 1:
            return [TreeNode(0)]
        ans = []
        for i in range(n):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n - 1 - i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)
        return ans
