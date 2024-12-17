from collections import Counter
from typing import List
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        def is_happy(group: int, remainders: List[int]) -> bool:
            for remainder in remainders:
                if gcd(group, remainder) != 1:
                    return False
            return True

        remainders = [i % batchSize for i in groups]
        remainders.sort()
        remainders = Counter(remainders)
        count = 0
        for remainder in remainders:
            count += remainders[remainder]
            if remainder == 0:
                continue
            if batchSize % remainder == 0:
                return count
            else:
                count += batchSize // remainder * remainders[batchSize % remainder]

        return count + sum(remainders[i] for i in range(1, batchSize // 2 + 1))

        def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
            groups.sort(reverse=True)
            count = 0
            for group in groups:
                if is_happy(group, groups):
                    count += 1
                    groups.remove(group)
                    batchSize -= group
                    if batchSize == 0:
                        break
            return count