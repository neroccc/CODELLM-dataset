from typing import List
class Solution:
    def partitionLabels(self, text: str) -> List[int]:
        last = {c: i for i, c in enumerate(text)}
        first = 0
        end = 0
        for i, c in enumerate(text):
            end = max(end, last[c])
            if i == end:
                yield end - first + 1
                first = i + 1