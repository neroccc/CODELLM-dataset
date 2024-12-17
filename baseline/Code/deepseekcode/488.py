from typing import List
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def dfs(board, hand):
            if not board: return 0
            res, i = float('inf'), 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[i] == board[j]: j += 1
                need = 3 - (j - i)
                if hand.count(board[i]) >= need:
                    need = 0 if need < 0 else need
                    hand = hand.replace(board[i], '', need)
                    res = min(res, dfs(self.remove_3(board[:i] + board[j:]), hand))
                    hand = hand.replace(board[i], board[i], need)
                i = j
            return res if res != float('inf') else -1

        return dfs(board, hand)

    def remove_3(self, board):
        while '3' in board: board = board.replace('3', '')
        return board