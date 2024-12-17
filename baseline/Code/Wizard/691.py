from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def isSubstring(s: str, t: str) -> bool:
            for i in range(len(s) - len(t) + 1):
                if s[i : i + len(t)] == t:
                    return True
            return False

        def dfs(target: str, memo: dict, stickers: List[str], count: int) -> int:
            if target in memo:
                return memo[target]
            if not target:
                return count
            if count == -1:
                memo[target] = -1
                return -1

            for sticker in stickers:
                if sticker[0] == target[0]:
                    if isSubstring(target, sticker):
                        memo[target] = min(
                            dfs(target[1:], memo, stickers, count + 1),
                            dfs(target, memo, stickers, count),
                        )
                    else:
                        memo[target] = dfs(target, memo, stickers, count + 1)
                    if memo[target] != -1:
                        return memo[target]

            memo[target] = -1
            return -1

        memo = {}
        return dfs(target, memo, stickers, 0)