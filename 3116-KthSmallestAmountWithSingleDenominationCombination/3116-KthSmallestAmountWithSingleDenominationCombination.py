# Last updated: 9/8/2025, 7:40:52 pm
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)

        def isGood(mid):
            total = 0
            for mask in range(1, 1 << n):
                bits = bin(mask).count('1')
                l = 1
                for i in range(n):
                    if mask >> i & 1:
                        l = lcm(l, coins[i])
                        if l > mid: break
                else:
                    total += (mid // l) if bits % 2 == 1 else -(mid // l)
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
