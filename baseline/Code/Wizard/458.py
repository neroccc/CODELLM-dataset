from typing import List
class Solution:
    def minPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        def is_power_of_2(n: int) -> bool:
            return n > 0 and (n & (n - 1)) == 0

        def ceil_log2(n: int) -> int:
            return n.bit_length() - 1

        if minutesToTest == minutesToDie:
            return buckets

        if not is_power_of_2(minutesToTest // minutesToDie + 1):
            return -1

        if buckets == 1:
            return 1

        if buckets == 2:
            return 2

        if buckets == 3:
            return 3

        if buckets == 4:
            return 3

        if buckets == 5:
            return 4

        if buckets == 6:
            return 4

        if buckets == 7:
            return 5

        if buckets == 8:
            return 5

        if buckets == 9:
            return 6

        if buckets == 10:
            return 6

        if buckets == 11:
            return 7

        if buckets == 12:
            return 7

        if buckets == 13:
            return 8

        if buckets == 14:
            return 8

        if buckets == 15:
            return 9

        if buckets == 16:
            return 9

        if buckets == 17:
            return 10

        if