from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(l, r):
            if l > r:
                return []
            if l == r:
                return [nums[l]]
            res = []
            for i in range(l, r + 1):
                left = helper(l, i - 1)
                right = helper(i + 1, r)
                for lval in left:
                    for rval in right:
                        if op[i] == "+":
                            res.append(lval + rval)
                        elif op[i] == "-":
                            res.append(lval - rval)
                        else:
                            res.append(lval * rval)
            return res

        nums = [int(x) for x in expression.split() if x != " "]
        op = [x for x in expression if x != " " and x != " "]
        return helper(0, len(nums) - 1)