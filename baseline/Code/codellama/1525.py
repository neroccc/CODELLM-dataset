from typing import List
class Solution:
    def numSplits(self, s: str) -> int:
        left_count = {}
        right_count = {}
        left = 0
        right = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in left_count:
                left_count[s[i]] = 0
            left_count[s[i]] += 1
            left += 1
            
            if s[~i] not in right_count:
                right_count[s[~i]] = 0
            right_count[s[~i]] += 1
            right += 1
            
            if left_count == right_count:
                ans += 1
                
        return ans