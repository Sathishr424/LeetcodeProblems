# Last updated: 21/5/2025, 6:06:10 am
class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        mini = lower
        maxi = lower
        prev = lower
        for num in diff:
            curr = prev+num
            mini = min(mini, curr)
            maxi = max(maxi, curr)
            prev = curr
        
        diff = lower-mini
        maxi += diff
        
        return max(0, upper-maxi+1)