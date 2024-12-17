from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        ans = []

        def compute(i, j):
            if expression[i] in "+-*":
                for k in range((i + 1, j, 2):
                    if expression[k] in "+-*":
                        left = compute(i, k - 1)
                        right = compute(k + 1, j)
                        for x in left:
                            for y in right:
                                if expression[k] == "+":
                                    ans.append(x + y)
                                elif expression[k] == "-":
                                    ans.append(x - y)
                                else:
                                    ans.append(x * y)

        def helper(i, j):
            if i == j:
                ans.append(int(expression[i]))
            else:
                compute(i, j)

        helper(0, n - 1)
        return ans