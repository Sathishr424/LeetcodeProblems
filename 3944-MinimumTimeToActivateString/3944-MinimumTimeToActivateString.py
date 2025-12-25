# Last updated: 12/25/2025, 7:10:30 PM
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        maxi = n * (n + 1) // 2
        if k > maxi: return -1

        l = 0
        r = n-1

        def isGood(mid):
            stars = sorted(order[:mid+1])
            prev = -1
            curr = 0 
            for index in stars:
                left = index - prev
                right = n - index

                curr += left * right
                prev = index
            
            # print(mid, stars, curr >= k)
            return curr >= k
        
        while l < r:
            mid = (l + r) // 2
            # print(l, mid, r)
            if isGood(mid):
                r = mid
            else:
                l = mid + 1

        return l
            
            
            