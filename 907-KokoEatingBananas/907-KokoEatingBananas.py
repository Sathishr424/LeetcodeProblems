# Last updated: 12/6/2025, 5:45:46 am
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            mid = (l+r) // 2
            if mid >= res: break

            curr = 0
            for p in piles:
                curr += ceil(p/mid)

            if curr <= h:
                res = mid
                r = mid-1
            else:
                l = mid+1
            
        return res