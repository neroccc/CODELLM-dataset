from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        def check(mid):
            cnt = 0
            i = 0
            while i < len(nums):
                j = i + 1
                while j < len(nums) and prefix[j] - prefix[i] <= mid:
                    j += 1
                if j == len(nums) and prefix[j] - prefix[i] <= mid:
                    return True
                if j == i + 1 and prefix[j] - prefix[i] > mid:
                    return False
                cnt += 1
                i = j
            return cnt <= k

        l, r = max(nums), prefix[-1]
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l