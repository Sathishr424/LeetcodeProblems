# Last updated: 25/7/2025, 3:32:14 pm
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def isGood(maxTime):
            s = 0
            for bat in batteries:
                s += min(maxTime, bat)
            return s // n >= maxTime
        
        l = 0
        r = sum(batteries)

        while l < r:
            mid = (l + r + 1) // 2
            if isGood(mid):
                l = mid
            else:
                r = mid - 1
        
        return l