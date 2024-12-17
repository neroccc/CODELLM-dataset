from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Refer to the algorithm description to generate a complete and efficient Python solution for the given Problem Description2

        # Problem Description2
        There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

        You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

        **Example 1:**

        **Input:** n = 4, flights = [[0,1,100],[1,2,100],[0,2,500],[2,3,600],[3,0,700]], src = 0, dst = 3, k = 1
        **Output:** 700
        **Explanation:**
        The graph is shown above.
        The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
        Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

        **Example 2:**

        **Input:** n = 3,