# Last updated: 21/5/2025, 6:06:49 am
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        mini = lower
        maxi = lower
        
        prev = lower
        for num in diff:
            curr = prev+num
            mini = cmin(mini, curr)
            maxi = cmax(maxi, curr)
            prev = curr
        
        diff = lower-mini
        maxi += diff
        
        return cmax(0, upper-maxi+1)