from typing import List
from deepseekcode.help.helphelp import helper808
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4750: return 1.0
        dp = [[0.0] * 200 for _ in range(200)]
        return helper808(n, n, dp)