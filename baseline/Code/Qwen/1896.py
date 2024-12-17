from typing import List
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def dfs(i, j):
            if expression[i] == '0' or expression[i] == '1':
                return expression[i], 1
            if expression[i] == '(':
                cnt = 1
                for k in range(i + 1, j):
                    if expression[k] == '(':
                        cnt += 1
                    elif expression[k] == ')':
                        cnt -= 1
                        if cnt == 0:
                            return dfs(i + 1, k)
            if expression[j] == '&':
                res, cnt = dfs(i + 1, j - 1)
                if res == '0':
                    return '1', cnt + 1
                if res == '1':
                    return '0', cnt
                return '1', cnt
            if expression[j] == '|':
                res, cnt = dfs(i + 1, j - 1)
                if res == '0':
                    return '0', cnt
                if res == '1':
                    return '1', cnt + 1
                return '0', cnt
            return '0', 0

        return dfs(0, len(expression) - 1)[1]