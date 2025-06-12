# Last updated: 12/6/2025, 5:42:48 am
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ret = 0
        tmp = 0
        for i in s:
            if i == 'L': tmp -=1
            else: tmp += 1
            if tmp == 0: ret += 1
        return ret