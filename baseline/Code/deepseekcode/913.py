from typing import List
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2
        dp = [[[DRAW for _ in range(N)] for _ in range(N)] for _ in range(2*N+1)]
        for t in range(2*N, -1, -1):
            for m in range(N):
                for c in range(N):
                    if t % 2 == 0:  # Mouse's turn
                        if m == c:
                            dp[t][m][c] = MOUSE
                        elif t == 2*N-1:
                            dp[t][m][c] = DRAW
                        else:
                            for child in graph[c]:
                                if dp[t+1][m][child] == MOUSE:
                                    dp[t][m][c] = MOUSE
                                    break
                            else:
                                dp[t][m][c] = CAT
                    else:  # Cat's turn
                        if m == c:
                            dp[t][m][c] = CAT
                        elif t == 2*N-1:
                            dp[t][m][c] = DRAW
                        else:
                            for child in graph[m]:
                                if dp[t+1][child][c] == CAT:
                                    dp[t][m][c] = CAT
                                    break
                            else:
                                dp[t][m][c] = MOUSE
        return dp[0][1][2]