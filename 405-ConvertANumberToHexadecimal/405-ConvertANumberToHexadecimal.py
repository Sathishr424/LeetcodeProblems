# Last updated: 12/6/2025, 5:49:47 am
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        if num < 0: num += (2 ** 32)
        ret = ""
        tmp = 'abcdef'
        while num > 0:
            val = num % 16
            ret += str(val if val <= 9 else tmp[val-10])
            num //= 16
        return ret[::-1]