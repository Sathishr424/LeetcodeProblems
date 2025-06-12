# Last updated: 12/6/2025, 5:42:19 am
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ret = 0
        while num != 0:
            if num%2 == 0: num = num/2
            else: num-=1
            ret += 1
        return ret
        