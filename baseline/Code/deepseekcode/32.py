from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)

        return max_len