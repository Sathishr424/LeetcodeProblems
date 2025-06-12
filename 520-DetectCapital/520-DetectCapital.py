# Last updated: 12/6/2025, 5:48:39 am
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        cnt = 0
        cnt += ord(word[0]) < 97
        first = cnt

        for i in range(1, n):
            cnt += ord(word[i]) < 97
        
        return cnt == 0 or cnt == n or (first and cnt == 1)
