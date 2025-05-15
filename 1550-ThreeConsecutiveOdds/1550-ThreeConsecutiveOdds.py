# Last updated: 15/5/2025, 10:31:38 pm
N = 37
cmax = lambda x, y: x if x > y else y
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0] * N
        max_group = 0

        for num in range(1, n+1):
            s = 0
            while num:
                s += num % 10
                num //= 10

            groups[s] += 1
            max_group = cmax(max_group, groups[s])
        
        ret = 0
        for num in range(1, N):
            ret += groups[num] == max_group
        
        return ret