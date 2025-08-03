# Last updated: 3/8/2025, 7:25:16 pm
class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        is_neg = x < 0
        x = abs(x)
        maxi = 2 ** 31 - 1
        rem = 0
        while x:
            can = maxi - ret * 10
            rem = x % 10
            x //= 10
            if rem >= can:
                if rem == can:
                    if is_neg and x: return 0
                else:
                    return 0
            ret = ret * 10 + rem
            rem = 0
        
        if is_neg:
            return -ret
        return ret