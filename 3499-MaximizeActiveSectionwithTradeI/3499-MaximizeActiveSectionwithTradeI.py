# Last updated: 16/6/2025, 3:51:00 am
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        total = 0
        for i in range(n):
            total += s[i] == '1'

        ret = total
        i = 0
        zeros = 0
        ones = 0
        while i < n:
            if s[i] == '0':
                j = i + 1
                while j < n and s[j] == '0':
                    j += 1

                curr = j - i
                if ones and zeros:
                    ret = max(ret, total + zeros + curr)

                zeros = curr
                ones = 0
                i = j
            else:
                j = i + 1
                while j < n and s[j] == '1':
                    j += 1
                
                ones = j - i
                i = j
        
        return ret
                
