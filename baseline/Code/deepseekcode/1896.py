from typing import List
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        n = len(expression)
        dp, dp2 = [0] * n, [0] * n
        op = []

        for i in range(n):
            if expression[i] == '(':
                op.append(i)
            elif expression[i] == ')':
                j = op.pop()
                if not op:
                    if expression[j + 1] == '&':
                        dp[j] = min(dp[j], dp[i - 1] + 1)
                        dp2[i - 1] = min(dp2[i - 1], dp[j] + 1)
                    elif expression[j + 1] == '|':
                        dp[i - 