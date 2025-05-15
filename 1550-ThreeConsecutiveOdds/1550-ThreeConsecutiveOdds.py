# Last updated: 15/5/2025, 10:12:38 pm
class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 0 0 0 0 0 
        # 0 0 0 0 0
        # 0 0 0 0 0

        groups = defaultdict(int)
        max_group = 0

        for num in range(1, n+1):
            tmp = num
            s = 0
            while num:
                s += num % 10
                num //= 10

            groups[s] += 1
            max_group = max(max_group, groups[s])
        ret = 0

        for num in groups:
            if groups[num] == max_group:
                ret += 1
        
        return ret


