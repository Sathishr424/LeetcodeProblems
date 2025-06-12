# Last updated: 12/6/2025, 5:34:04 am
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        prefix_ones = 0
        index = n
        for i in range(n):
            if s[i] == '0':
                index = i
                break
            else:
                prefix_ones += 1
        
        prev_zero = index
        ones = 0
        ret = 0
        zeros = 1

        for i in range(index+1, n):
            if s[i] == '1':
                ones += 1
                prev_zero = n
            else:
                prev_zero = min(prev_zero, i)
                if ones:
                    ret = max(ret, zeros+1)
                    if i+1 == n or s[i+1] == '1':
                        zeros = i-prev_zero
                        prev_zero = i-zeros
                
                zeros += 1
        
        return ret+prefix_ones+ones
