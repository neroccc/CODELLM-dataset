import bisect
from typing import List
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = [int(d) for d in digits]
        d_len = len(digits)
        digits.append(float("inf"))
        ans = 0
        for i in range(len(str(n))):
            d_idx = bisect.bisect_right(digits, int(str(n)[i]))
            ans += (d_idx - 1) * (10 ** (d_len - 1 - i))
            if d_idx < d_len and digits[d_idx] == int(str(n)[i]):
                ans += (d_len - d_idx) * (10 ** (d_len - 1 - i))
        return ans + 1