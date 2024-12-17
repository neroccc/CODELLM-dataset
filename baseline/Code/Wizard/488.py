from typing import List
class Solution:
    def minInsertions(self, board: str, hand: str) -> int:
        def remove_groups(s: str) -> str:
            stack = []
            for c in s:
                if not stack or stack[-1] != c:
                    stack.append(c)
                else:
                    stack.pop()
            return ''.join(stack)

        def count_groups(s: str) -> int:
            return s.count('R') // 3 + s.count('Y') // 3 + s.count('B') // 3 + s.count('G') // 3

        board = remove_groups(board)
        hand = remove_groups(hand)
        n_board = len(board)
        n_hand = len(hand)