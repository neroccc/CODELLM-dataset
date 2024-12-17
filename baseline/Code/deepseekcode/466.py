from typing import List
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        len1, len2 = len(s1), len(s2)
        start, end = {}, {}
        j, cnt = 0, 0

        for k in range(n1):
            for i in range(len1):
                if s1[i] == s2[j]:
                    if j == len2 - 1:
                        cnt += 1
                        j = 0
                    else:
                        j += 1
            start[k] = (j, cnt)
            for m in range(k):
                if start[m] == (j, cnt):
                    pre_len = k - m
                    pre_cnt = cnt - m
                    loop_len = (n1 - m) // pre_len
                    loop_cnt = (n1 - m) // pre_len * pre_cnt
                    rest_len = (n1 - m) % pre_len
                    for l in range(m, n1):
                        if l % pre_len == rest_len:
                            return (loop_cnt + cnt - l // pre_len * pre_cnt) // n2
                    return (loop_cnt + cnt) // n2

        return cnt // n2