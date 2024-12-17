import math
from typing import List
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        S = str(n)
        m, k = len(S), 0

        # Count the numbers with no repeated digits
        for i in range(1, m):
            k += 9 * math.perm(9, i)

        # Use a set to record the digits that have been used
        used = set()

        # Iterate over the digits in the given number
        for i in range(len(S)):
            if i == 0:
                # The first digit can't be 0
                for j in range(1, int(S[i])):
                    if j not in used:
                        k += math.perm(9, m - 1)
            else:
                # Enumerate the possible digits for the current position
                for j in range(int(S[i])):
                    if j not in used:
                        k += math.perm(9, m - i - 1)

            if S[i] in used:
                break
            used.add(int(S[i]))

        # Subtract the numbers with no repeated digits from n
        return n - k