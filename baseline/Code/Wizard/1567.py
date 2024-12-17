from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 1
        max_len = 1
        temp_product = 1
        temp_len = 1
        temp_max = nums[0]
        temp_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp_product, temp_len = temp_min, temp_len
            temp_max = max(temp_max * nums[i], nums[i])
            temp_min = min(temp_min * nums[i], nums[i])
            temp_product = max(temp_max, temp_product)
            max_product = max(max_product, temp_product)
            temp_len += 1
            max_len = max(max_len, temp_len)

        return max_len