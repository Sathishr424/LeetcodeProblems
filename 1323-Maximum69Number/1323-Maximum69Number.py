# Last updated: 16/8/2025, 9:15:39 am
class Solution:
    def maximum69Number (self, num: int) -> int:
        def rec(num):
            if num == 0: return 0
            to_pass = num // 10
            ret = rec(to_pass)
            if ret == to_pass:
                if num % 10 == 6:
                    return to_pass * 10 + 9
                return num
            else:
                return ret * 10 + (num % 10)
        
        return rec(num)