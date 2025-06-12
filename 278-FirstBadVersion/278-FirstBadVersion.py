# Last updated: 12/6/2025, 5:50:57 am
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def sub(l, r):
            if l >= r: return l
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
            return sub(l, r)
        return sub(1, n)