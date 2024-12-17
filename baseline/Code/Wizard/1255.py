from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def is_valid(word, letters, score):
            letter_count = [0] * 26
            for letter in word:
                letter_count[ord(letter) - ord('a')] += 1
            for i in range(26):
                if letter_count[i] > letters.count(chr(ord('a') + i)):
                    return False
            return True

        def word_score(word, score):
            return sum([score[ord(letter) - ord('a')] for letter in word])

        words = [word for word in words if is_valid(word, letters, score)]
        words.sort(key=lambda x: -word_score(x, score))
        max_score = 0
        letter_count = [0] * 26
        for word in words:
            for letter in word:
                letter_count[ord(letter) - ord('a')] += 1
            if all(letter_count[i] >= 0 for i in range(26)):
                max_score = max(max_score, word_score(word, score))
                for i in range(26):
                    letter_count[i] -= ord(word[0]) - ord('a')
        return max_score