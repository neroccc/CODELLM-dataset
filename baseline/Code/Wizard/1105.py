from typing import List
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * n
        max_height = 0

        for i in range(n):
            dp[i] = books[i][1]
            width = books[i][0]

            for j in range(i):
                if width + books[j][0] <= shelfWidth:
                    dp[i] = max(dp[i], dp[j] + books[i][1])
                    width += books[j][0]

            max_height = max(max_height, dp[i])

        return max_height