import math
from typing import List
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        memo = {0: 0, 1: cost(x, 1)}
        return dp(x, target, memo) - 1

def dp(x, target, memo):
    if target in memo: return memo[target]
    k = int(math.log(target) / math.log(x))
    c1 = cost(x, k) + dp(x, target - pow(x, k), memo)
    c2 = cost(x, k + 1) + dp(x, pow(x, k + 1) - target, memo)
    memo[target] = min(c1, c2) if target - pow(x, k) < pow(x, k + 1) - target else c2
    return memo[target]

def cost(x, k):
    return k + (k - 1) if x > k > 0 else k