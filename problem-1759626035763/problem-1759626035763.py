# Last updated: 5/10/2025, 6:30:35 am
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort()

        def isGood(mid):
            prev = price[0]
            cnt = 1
            for i in range(1, n):
                if price[i] - prev >= mid:
                    cnt += 1
                    prev = price[i]
            return cnt >= k
        
        l = 0
        r = price[-1] - price[0]

        while l < r:
            mid = (l + r + 1) // 2

            if isGood(mid):
                l = mid
            else:
                r = mid - 1

        return l