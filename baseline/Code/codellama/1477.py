from typing import List
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = 0
        right = 0
        curr_sum = 0
        min_len = float('inf')
        while right < n:
            while curr_sum < target and right < n:
                curr_sum += arr[right]
                right += 1
            
            while curr_sum > target and left < right:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                min_len = min(min_len, right - left)
            
            if right == n:
                break
            
            curr_sum -= arr[right]
            right += 1
        
        return min_len if min_len != float('inf') else -1
