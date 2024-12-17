from typing import List
class Solution:
    def heightChecker(self, books: List[List[int]]) -> int:
        n = len(books)
        ans = [0] * n
        for i in range(n):
            ans[i] = books[i][0] * books[i][1]
        ans.sort()
        ans2 = [0] * n
        for i in range(n):
            ans2[i] = ans[i]
        ans = ans2
        ans2 = [0] * n
        for i in range(n):
            ans2[i] = books[i][1]
        ans2.sort()
        ans3 = [0] * n
        for i in range(n):
            ans3[i] = ans2[i]
        ans2 = ans3
        ans3 = [0] * n
        for i in range(n):
            ans3[i] = ans[i]
        ans = ans3
        return sum(ans)