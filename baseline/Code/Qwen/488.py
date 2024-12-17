from typing import List
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_groups(board):
            i = 0
            while i < len(board):
                count = 1
                while i + 1 < len(board) and board[i] == board[i + 1]:
                    i += 1
                    count += 1
                if count >= 3:
                    return board[:i - count + 1] + board[i + 1:]
                i += 1
            return board

        def dfs(board, hand):
            if not board:
                return 0
            if not hand:
                return float('inf')
            ans = float('inf')
            for i in range(len(hand)):
                for j in range(len(board) + 1):
                    new_board = board[:j] + hand[i] + board[