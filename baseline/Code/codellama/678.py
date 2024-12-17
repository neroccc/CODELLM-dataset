from typing import List
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = right = max_stars = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right -= 1
                max_stars = max(max_stars - 1, left - right)
                if max_stars < 0:
                    return False
            else:
                left += 1
                right += 1
                max_stars += 1
        return left == right == max_stars == 0