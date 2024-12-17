from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        dp = [0] + [float('inf')] * time
        for i in range(1, time + 1):
            for start, end in clips:
                if start < i:
                    dp[i] = min(dp[i], dp[start] + 1)
                else:
                    break
        return dp[-1] if dp[-1] < float('inf') else -1