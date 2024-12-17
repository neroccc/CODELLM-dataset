from typing import List
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def helper(a, b):
            count = 0
            diff = [[0]*len(b) for _ in range(len(a))]
            for i in range(len(a)):
                for j in range(len(b)):
                    if i > 0 and j > 0:
                        diff[i][j] = diff[i-1][j-1]
                    if a[i] != b[j]:
                        diff[i][j] += 1
                    if diff[i][j] == 1:
                        count += 1
            return count

        return helper(s, t) - helper(t, s)