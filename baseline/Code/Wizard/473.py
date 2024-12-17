from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        avg_length = total_length // 4
        matchsticks.sort(reverse=True)

        def dfs(used, i, side_lengths):
            if i == len(matchsticks):
                return all(length == side_lengths[0] for length in side_lengths)

            for j in range(i, len(matchsticks)):
                if used[j]:
                    continue
                if matchsticks[j] > avg_length:
                    continue

                used[j] = True
                if dfs(used, i, [length + matchsticks[j] for length in side_lengths]):
                    return True
                used[j] = False

            return False

        return dfs([False] * len(matchsticks), 0, [0] * 4)