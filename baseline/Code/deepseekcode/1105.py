from typing import List
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [10000] * n

        for i in range(1, n + 1):
            max_height = 0
            total_width = 0
            j = i
            while j > 0:
                total_width += books[j - 1][0]
                if total_width > shelfWidth:
                    break
                max_height = max(max_height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + max_height)
                j -= 1

        return dp[-1]