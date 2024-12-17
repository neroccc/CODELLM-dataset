from typing import List
class Solution:
    def minOperations(self, expression: str) -> int:
        stack = []
        count = 0
        for char in expression:
            if char == '(':
                stack.append(count)
                count = 0
            elif char == ')':
                count += stack.pop()
            elif char == '|':
                count += 1
            elif char == '&':
                count += 1
            elif char == '0':
                count += 1
            elif char == '1':
                count += 0
        return count