from typing import List
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        
        count = 0
        for i in range(1, n + 1):
            count += self.countDigitOneInNumber(i)
        
        return count
    
    def countDigitOneInNumber(self, num: int) -> int:
        count = 0
        while num > 0:
            digit = num % 10
            if digit == 1:
                count += 1
            num //= 10
        
        return count