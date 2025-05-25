# Last updated: 25/5/2025, 11:38:38 am
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        there = Counter(words)
        
        ret = 0
        odd = False

        for word in there:
            if word[0] == word[1]:
                odd = odd or (there[word] % 2 == 1)
                ret += there[word] - (there[word] % 2)
            else:
                ret += min(there[word], there[word[1] + word[0]])

        return (ret + odd) * 2