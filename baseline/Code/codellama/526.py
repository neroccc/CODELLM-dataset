from typing import List
class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(pos, used, used_count):
            if pos == n + 1:
                return 1
            
            count = 0
            for i in range(1, n + 1):
                if used[i] or (i % pos != 0 and pos % i != 0):
                    continue
                
                used[i] = True
                used_count[i] = True
                count += dfs(pos + 1, used, used_count)
                used[i] = False
                used_count[i] = False
            
            return count
        
        used = [False] * (n + 1)
        used_count = [False] * (n + 1)
        return dfs(1, used, used_count)
