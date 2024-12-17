from typing import Optional, List, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()

    return result

def helper808(self, a, b, dp):
        if a <= 0 and b <= 0: return 0.5
        if a <= 0: return 1.0
        if b <= 0: return 0.0
        if dp[a][b]: return dp[a][b]
        dp[a][b] = 0.25 * (self.helper(a - 100, b, dp) + self.helper(a - 75, b - 25, dp) + self.helper(a - 50, b - 50, dp) + self.helper(a - 25, b - 75, dp))
        return dp[a][b]

def get_last_event(events, i):
        while i >= 0:
            if events[i][1] > events[-1][0]:
                i -= 1
            else:
                return i
        return -1

def gcd(self, x: int, y: int) -> int:
        return x if y == 0 else self.gcd(y, x % y)
def isSubsequence(word, s):
        i = 0
        for c in s:
            if i < len(word) and word[i] == c:
                i += 1
        return i == len(word)
def check_subset_sum(nums, target, k):
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(k + 1)]

        for i in range(n):
            dp[1][nums[i]] = True

        for i in range(2, k + 1):
            for j in range(target + 1):
                for l in range(i - 1, n):
                    if j >= nums[l] and dp[i - 1][j - nums[l]]:
                        dp[i][j] = True
                        break

        return dp[k][target]
def dfs1723(self, jobs, k, idx, workers):
        if idx == len(jobs):
            self.ans = min(self.ans, max(workers))
            return

        if max(workers) >= self.ans:
            return

        for i in range(k):
            workers[i] += jobs[idx]
            self.dfs(jobs, k, idx + 1, workers)
            workers[i] -= jobs[idx]

            if workers[i] == 0:
                break