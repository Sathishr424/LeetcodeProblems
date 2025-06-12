# Last updated: 12/6/2025, 5:50:11 am
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            mid = (l+r)//2

            if mid * mid < num:
                l = mid+1
            else:
                r = mid-1
        
        return l * l == num