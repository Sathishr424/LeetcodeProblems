# Last updated: 12/6/2025, 5:41:44 am
class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        if s[0] == '0':
            zeros += 1
        else:
            ones -= 1
        
        res = zeros + ones
        
        for i in range(1, len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            res = max(res, zeros + ones)
        
        return res
