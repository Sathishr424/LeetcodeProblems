# Last updated: 16/6/2025, 3:52:40 am
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        total = 0
        for i in range(n):
            total += s[i] == '1'

        ret = total
        i = 0
        zeros = 0
        ones = False
        while i < n:
            if s[i] == '0':
                j = i + 1
                while j < n and s[j] == '0':
                    j += 1

                curr = j - i
                if ones and zeros:
                    ret = max(ret, total + zeros + curr)

                zeros = curr
                ones = False
                i = j
            else:
                ones = True
                i += 1
                while i < n and s[i] == '1':
                    i += 1
                
        return ret
                
