from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        dp = [float('inf')] * (time + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(clips[i][0], clips[i][1] + 1):
                if j > dp[j - 1]:
                    dp[j] = dp[j - 1] + 1
        return dp[time] if dp[time] != float('inf') else -1
