# Last updated: 12/6/2025, 5:42:49 am
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        tot = sum(candies)
        if tot < k: return 0

        l = 1
        r = tot//k
        while l < r:
            candy = (l+r) // 2 + 1
            
            used = 0
            for c in candies:
                used += c // candy
            
            if used >= k:
                l = candy
            else:
                r = candy-1
        
        return l