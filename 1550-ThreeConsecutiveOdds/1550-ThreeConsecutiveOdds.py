# Last updated: 15/5/2025, 10:29:40 pm
N = 37
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
            max_group = max(max_group, groups[s])
        
        ret = 0
        for num in range(1, N):
            if groups[num] == max_group:
                ret += 1
        
        return ret


