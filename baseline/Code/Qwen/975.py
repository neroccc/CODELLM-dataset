from typing import List
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher = [None] * n
        next_lower = [None] * n
        stack = []

        for num, i in sorted([num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for num, i in sorted([-num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher = [False] * n
        lower = [False] * n
        higher[-1] = lower[-1] = True

        for i in range(n - 2, -1, -1):
            higher[i] = lower[next_higher[i]] if next_higher[i] is not None else False
            lower[i] = higher[next_lower[i]] if next_lower[i] is not None else False

        return sum(higher)