from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: int, right: int, op: str) -> List[int]:
            res = []
            for i in range(left, right):
                if expression[i] in "+-*":
                    left_res = cache[left][i]
                    right_res = cache[i + 1][right]
                    for l in left_res:
                        for r in right_res:
                            if op == "+":
                                res.append(l + r)
                            elif op == "-":
                                res.append(l - r)
                            else:
                                res.append(l * r)
            return res

        cache = [[[] for _ in range(len(expression))] for _ in range(len(expression))]
        for i in range(len(expression)):
            if expression[i].isdigit():
                cache[i][i] = [int(expression[i])]
            else:
                for j in range(i + 1, len(expression)):
                    if expression[j].isdigit():
                        cache[i][j] = compute(i, j, expression[j])
        return cache[0][-1]