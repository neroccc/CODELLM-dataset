from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Count the frequency of each letter in the given letters
        freq = [0] * 26
        for ch in letters:
            freq[ord(ch) - ord('a')] += 1

        # Calculate the score of each word
        word_scores = []
        for word in words:
            word_score = 0
            word_freq = [0] * 26
            for ch in word:
                word_score += score[ord(ch) - ord('a')]
                word_freq[ord(ch) - ord('a')] += 1
            word_scores.append((word_score, word_freq))

        # Use dynamic programming to find the maximum score
        dp = [0] * (1 << 14)
        for mask in range(1, 1 << len(words)):
            word_freq = [0] * 26
            for i in range(len