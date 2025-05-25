# Last updated: 25/5/2025, 11:31:23 am
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        there = defaultdict(int)
        
        for word in words:
            there[word] += 1
        
        ret = 0
        odd = False

        for word in there:
            if there[word] == 0: continue
            reverse_word = word[::-1]
            if word[0] == word[1]:
                odd = odd or (there[word] % 2 == 1)
                ret += there[word] - (there[word] % 2)
            elif reverse_word in there:
                ret += min(there[word], there[reverse_word]) * 2
                there[reverse_word] = 0

        return (ret + odd) * 2