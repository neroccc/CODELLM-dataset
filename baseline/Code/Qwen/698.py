from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target_sum = total_sum // k
        nums.sort(reverse=True)
        if nums[0] > target_sum:
            return False

        visited = [False] * len(nums)
        return self.dfs(nums, visited, 0, 0, target_sum, k)

    def dfs(self, nums, visited, current_sum, index, target_sum, k):
        if k == 1:
            return True

        if current_sum == target_sum:
            return self.dfs(nums, visited, 0, 0, target_sum, k - 1)

        for i in range(index, len(nums)):
            if not visited[i] and current_sum + nums[i] <= target_sum:
                visited[i] = True
                if self.dfs(nums, visited, current_sum + nums[i], i + 1, target_sum, k):
                    return True
                visited[i] = False

        return False