from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == ')':
                if not stack or stack[-1] == '(':
                    stack.pop()
                elif stack[-1] == ')':
                    stack.pop()
                    stack.append(')')
            else:
                stack.append('(')

        return not stack