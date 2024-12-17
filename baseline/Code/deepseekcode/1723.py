from typing import List
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
        l, r = max(jobs), sum(jobs)

        def check(limit):
            def dfs(idx, workload):
                if idx == n:
                    return True
                cur = jobs[idx]
                for i in range(len(workload)):
                    if workload[i] + cur <= limit:
                        workload[i] += cur
                        if dfs(idx + 1, workload):
                            return True
                        workload[i] -= cur
                    if workload[i] == 0:
                        break
                return False

            return dfs(0, [0] * k)

        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l