from typing import List
class Solution:
    def countArrangement(self, n: int) -> int:
        def calculate(num, X):
            if len(X) == 1: return 1
            total = 0
            for i in range(len(X)):
                if X[i] % num == 0 or num % X[i] == 0:
                    total += calculate(num - 1, X[:i] + X[i+1:])
            return total
        return calculate(n, tuple(range(1, n + 1)))