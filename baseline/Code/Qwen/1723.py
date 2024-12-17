from typing import List
from deepseekcode.help.helphelp import dfs1723


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
        workers = [0] * k
        ans = float('inf')
        return dfs1723(jobs, k, 0, workers, ans)

