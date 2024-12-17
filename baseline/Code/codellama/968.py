from typing import List
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 2
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.need_camera[node] = 1
                return 1
            if left == 1 or right == 1:
                self.need_camera[node] = 0
                return 0
            self.need_camera[node] = 1
            return 2
        
        self.need_camera = defaultdict(int)
        ans = 0
        if not root or dfs(root) == 1:
            ans += 1
        return ans + sum(self.need_camera.values())
