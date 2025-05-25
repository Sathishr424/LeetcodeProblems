# Last updated: 25/5/2025, 11:27:38 am
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        there = defaultdict(int)

        for word in words:
            there[word] += 1
        
        ret = 0
        vis = {}
        odd = False
        for word in there:
            if word in vis: continue
            rev = word[::-1]
            if word != rev and rev in there and there[rev] and there[word]:
                cnt = min(there[word], there[rev])
                ret += cnt * 2
                vis[rev] = 1
            elif word[0] == word[1]:
                odd = odd or (there[word] % 2 == 1)
                ret += there[word] - (there[word] % 2)

        if odd: ret += 1

        return ret * 2