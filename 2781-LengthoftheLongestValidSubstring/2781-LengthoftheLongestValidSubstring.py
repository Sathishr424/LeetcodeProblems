# Last updated: 29/7/2025, 11:55:41 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        remove = set(forbidden)
        word = list(word)
        
        def check(l, r):
            m = len(word)
            curr = ''
            for i in range(r, max(l - 1, r - 10), -1):
                curr = word[i] + curr
                if curr in remove: return i
            return -1

        ret = 0
        left = 0
        l = 0
        for i in range(n):
            index = check(left, i)
            if index != -1:
                left = index + 1
            ret = cmax(ret, i - left + 1)
        
        return ret