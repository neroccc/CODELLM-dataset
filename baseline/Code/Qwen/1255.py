from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def dfs(i, curr_score):
            if i == len(words):
                return curr_score
            
            # Skip the current word
            res = dfs(i + 1, curr_score)
            
            # Check if the current word can be formed with the available letters
            if all(letters_count[c] >= count for c, count in words_count[i].items()):
                # Update the available letters count
                for c, count in words_count[i].items():
                    letters_count[c] -= count
                
                # Recurse with the updated score
                res = max(res, dfs(i + 1, curr_score + words_score[i]))
                
                # Restore the available letters count
                for c, count in words_count[i].items():
                    letters_count[c] += count
            
            return res
        
        # Precompute the score of each word
        words_score = [sum(score[ord(c