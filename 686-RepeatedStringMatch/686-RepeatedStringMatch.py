# Last updated: 24/6/2025, 5:30:50 pm
inf = float('inf')
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        
        # def getKMP(word):
        #     n = len(word)
        #     lps = [0] * n
            
        #     i = 1
        #     j = 0
        #     while i < n:
        #         if word[i] == word[j]:
        #             j += 1
        #             lps[i] = j
        #         elif j > 0:
        #             j = lps[j - 1]
        #             continue
        #         i += 1
        #     return lps

        # lps = getKMP(b)
        ret = inf
        for i in range(n):
            if a[i] == b[0]:
                l = m - (n - i)
                to_add = ceil(l / n)
                new_a = a + (a * to_add)
                # print(new_a)
                if new_a[i:i+m] == b:
                    ret = min(ret, to_add + 1)
        
        return -1 if ret == inf else ret
