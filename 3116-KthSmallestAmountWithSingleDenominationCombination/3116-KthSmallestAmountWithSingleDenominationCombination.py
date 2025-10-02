# Last updated: 3/10/2025, 2:36:02 am
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        coins.sort()

        def isGood(mid):
            total = 0
            for mask in range(1, 1 << n):
                bits = mask.bit_count()

                LCM = 1
                for i in range(n):
                    if mask & (1 << i):
                        LCM = lcm(LCM, coins[i])
                        if LCM > mid: break
                
                if bits % 2:
                    total += mid // LCM
                else:
                    total -= mid // LCM
            
            return total >= k

        l = 1
        r = coins[0] * k

        while l < r:
            mid = (l + r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
