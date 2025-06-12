# Last updated: 12/6/2025, 5:48:47 am
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        ret = ""
        if num < 0: 
            ret += '-'
            num = abs(num)
        
        def helper(n, s):
            if n == 0: return s
            s = helper(n // 7, s)
            s += str(n % 7)
            return s
        
        return helper(num, ret)