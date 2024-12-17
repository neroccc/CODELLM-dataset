from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n = len(clips)
        dp = [float('inf')] * (time + 1)
        dp[0] = 0

        for i in range(n):
            start, end = clips[i]
            if start > time:
                break
            for j in range(start, end + 1):
                if j > time:
                    break
                dp[j] = min(dp[j], dp[start] + 1)

        return dp[time] if dp[time] != float('inf') else -1