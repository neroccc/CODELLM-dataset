from typing import List
class Solution:
    def minDays(self, n: int) -> int:
        from collections import deque
        q = deque([(n, 0)])
        seen = {n}
        while q:
            cur, step = q.popleft()
            if cur == 0:
                return step
            for nxt in (cur - 1, cur // 2, cur // 3):
                if nxt not in seen and 0 <= nxt:
                    q.append((nxt, step + 1))
                    seen.add(nxt)