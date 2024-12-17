from typing import List
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        nums = [0, 1, 1]
        for i in range(3, n + 1):
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[i // 2] + nums[i // 2 + 1])
        return nums[-1]
    
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        nums = [0, 1, 1]
        for i in range(3, n + 1):
            nums.append(nums[i // 2] + (nums[i // 2 + 1] if i % 2 == 0 else 0))
        return nums[-1]
    
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        nums = [0, 1, 1]
        for i in range(3, n + 1):
            nums.append(nums[i // 2] + (nums[i // 2 + 1] if i % 2 == 0 else 0))
        return nums[-1]
    
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        nums = [0, 1, 1]
        for i