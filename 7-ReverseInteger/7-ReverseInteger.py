# Last updated: 12/6/2025, 5:55:37 am
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if (x.find('-') != -1): 
            x = x[1:]
            if (-int(x[::-1]) < -2147483648): return 0
            return -int(x[::-1])
        if (int(x[::-1]) > 2147483648): return 0
        return int(x[::-1])