# Last updated: 12/6/2025, 5:41:57 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0] * 37
        max_group = 0

        for num in range(1, n+1):
            s = 0
            while num:
                s += num % 10
                num //= 10

            groups[s] += 1
            max_group = cmax(max_group, groups[s])
        
        ret = 0
        for num in groups:
            ret += num == max_group
        
        return ret