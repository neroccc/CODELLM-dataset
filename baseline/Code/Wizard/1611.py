from typing import List
class Solution:
    def minOperations(self, n: int) -> int:
        binary = bin(n)[2:]
        count = 0
        for i in range(1, len(binary)):
            if binary[i] == '1' and binary[i-1] == '1':
                count += 1
        return count + len(binary) - 1