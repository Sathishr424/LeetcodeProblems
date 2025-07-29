# Last updated: 29/7/2025, 11:33:40 pm
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
        i = 0
        while i < n:
            curr += word[i]
            index = check(curr)
            if index != -1:
                curr = curr[index+1:]
            # print(i, curr)
            ret = max(ret, len(curr))
            i += 1
        
        return ret
            