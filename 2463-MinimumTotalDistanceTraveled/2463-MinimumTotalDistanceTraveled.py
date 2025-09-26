# Last updated: 27/9/2025, 4:23:41 am
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        r = len(robot)
        f = len(factory)

        robot.sort()

        fac = []
        for i in range(f):
            for _ in range(factory[i][1]):
                fac.append(factory[i][0])
        
        fac.sort()

        @cache
        def rec(i, j):
            if i == -1: return 0
            if j == -1: return inf

            ans = rec(i-1, j-1) + abs(robot[i] - fac[j])
            return min(ans, rec(i, j-1))
        
        ans = rec(r-1, len(fac)-1)
        rec.cache_clear()
        return ans