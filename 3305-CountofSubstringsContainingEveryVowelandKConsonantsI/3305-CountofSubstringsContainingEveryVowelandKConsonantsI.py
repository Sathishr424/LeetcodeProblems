# Last updated: 5/7/2025, 1:04:20 am
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ret = 0
        for i in range(n):
            vowels = {}
            cons = 0
            for j in range(i, n):
                if word[j] in 'aeiou':
                    vowels[word[j]] = 1
                else:
                    cons += 1
                if len(vowels) == 5 and cons == k:
                    ret += 1
        
        return ret