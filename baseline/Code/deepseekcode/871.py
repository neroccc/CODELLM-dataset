from typing import List
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append([target, 0])
        ans = prev = 0
        for position, fuel in stations:
            startFuel -= position - prev
            while startFuel < 0 and pq:
                startFuel += -heapq.heappop(pq)
                ans += 1
            if startFuel < 0:
                return -1
            heapq.heappush(pq, -fuel)
            prev = position
        return ans