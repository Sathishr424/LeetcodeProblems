# Last updated: 29/7/2025, 11:35:43 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        remove = set(forbidden)
        
        def check(word):
            m = len(word)
            for j in range(m-1, max(-1, m-10-1), -1):
                if word[j:] in remove: return j
            return -1

        ret = 0
        curr = ''
        l = 0
        for i in range(n):
            curr += word[i]
            index = check(curr)
            if index != -1:
                curr = curr[index+1:]
                l = 0
            if len(curr) > 10:
                curr = curr[1:]
                l += 1
            ret = cmax(ret, l + len(curr))
        
        return ret
            