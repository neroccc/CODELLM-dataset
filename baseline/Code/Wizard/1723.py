from typing import List
class Solution:
    def minMaxSum(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        total_sum = sum(jobs)
        n = len(jobs)
        ans = 0

        for i in range(k):
            ans += jobs[i]

        for i in range(k, n):
            if jobs[i] > jobs[k - 1]:
                ans += jobs[i] - jobs[k - 1]

        return ans