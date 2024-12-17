from typing import List
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        ans = 0
        index = {}
        for i in range(n):
            if s[i] in index:
                index[s[i]].append(i)
            else:
                index[s[i]] = [i]

        for key in index:
            arr = index[key]
            arr.append(n)
            for i in range(len(arr) - 1):
                ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])

        return ans