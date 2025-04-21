# Last updated: 21/4/2025, 2:03:22 pm
class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        prev = diff[0]
        mini = prev
        maxi = prev
        for d in diff:
            curr = prev+d
            if curr < mini: mini = curr
            elif curr >= maxi: maxi = curr
            prev = curr

        l = lower-mini
        r = maxi+l
        
        return max(0, upper-r+1)