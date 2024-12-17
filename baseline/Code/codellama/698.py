from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        def dfs(idx, cur_sum, k):
            if k == 0:
                return True
            if cur_sum == target:
                return dfs(0, 0, k - 1)
            for i in range(idx, len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                if dfs(i + 1, cur_sum + nums[i], k):
                    return True
                visited[i] = False
            return False
        return dfs(0, 0, k)