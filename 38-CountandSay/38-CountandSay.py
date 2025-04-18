# Last updated: 18/4/2025, 6:51:19 am
class Solution:
    @cache
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'

        before = self.countAndSay(n-1)
        prev = before[0]
        cnt = 1
        ret = ''
        for i in range(1, len(before)):
            if before[i] == prev:
                cnt += 1
            else:
                ret += f"{cnt}{prev}"
                cnt = 1
            prev = before[i]
                
        ret += f"{cnt}{prev}"
        return ret