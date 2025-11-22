# Last updated: 22/11/2025, 9:25:31 pm
class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        total = n * (n + 1) / 2

        if total < target: return []
        if -total > target: return []
        if total == target: return [i for i in range(1, n+1)]

        
        rem = 0
        ret = []
        used = {}
        other = total
        for i in range(n, 0, -1):
            if -(rem + i) + (other - i) >= target:
                rem += i
                used[i] = 1
                other -= i

        if (-rem)+other != target: return []
        for i in range(1, n + 1):
            if i not in used:
                ret.append(i)

        for num in used:
            ret.append(-num)

        ret.sort()
        return ret