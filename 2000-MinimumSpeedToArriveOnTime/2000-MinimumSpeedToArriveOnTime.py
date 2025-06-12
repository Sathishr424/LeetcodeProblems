# Last updated: 12/6/2025, 5:39:34 am
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour): return -1
        l = 1
        r = 10**7
        res = r

        while l <= r:
            mid = (r+l) // 2
            # print(l, mid, res)
            curr_hour = 0
            for d in dist:
                curr_hour = ceil(curr_hour)
                curr_hour += d/mid
            # print(curr_hour)
            if curr_hour <= hour:
                r = mid-1
                res = mid
            else:
                l = mid+1
        
        return res