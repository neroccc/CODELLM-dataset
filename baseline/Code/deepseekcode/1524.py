from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [0] * (len(arr) + 1)
        count = [0] * (len(arr) + 1)
        odd = [0] * (len(arr) + 1)
        even = [0] * (len(arr) + 1)
        odd[0] = 1
        for i in range(len(arr)):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
            if prefix_sum[i + 1] % 2 == 0:
                even[i + 1] = even[i] + 1
                odd[i + 1] = odd[i]
            else:
                even[i + 1] = odd[i]
                odd[i + 1] = even[i] + 1
            count[i + 1] = (count[i] + even[i + 1]) % (10**9 + 7)
        return count[-1]