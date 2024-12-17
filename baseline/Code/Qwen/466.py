from typing import List
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_idx = 0
        s2_idx = 0
        s2_count = 0
        s2_count_map = {}

        while True:
            if (s1_idx, s2_idx) in s2_count_map:
                loop_start_idx = s2_count_map[(s1_idx, s2_idx)]
                loop_len = s2_count - loop_start_idx
                loop_s2_idx = s2_idx
                loop_s2_count = s2_count
                break
            else:
                s2_count_map[(s1_idx, s2_idx)] = s2_count

            for _ in range(s1_len):
                if s1[s1_idx] == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == s2_len:
                        s2_idx = 0
                        s2_count += 1
                s1_idx += 1
                if s1_idx == s1_len:
                    s1_idx = 0

        total_s2_count = s2_count + (n1 - 1) * loop_len
        remainder = n1 % loop_len
        for _ in range(remainder):
            for _ in range(s1_len):
                if s1[s1_idx] == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == s2_len:
                        s2_idx = 0
                        total_s2_count += 1
                s1_idx += 1
                if s1_idx == s1_len:
                    s1_idx