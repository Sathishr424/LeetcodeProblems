# Last updated: 9/8/2025, 7:57:53 pm
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)

        odd_lcm = []
        even_lcm = []

        for mask in range(1, 1 << n):
            l = 1
            count = 0

            for i in range(n):
                if mask & (1 << i) > 0:
                    l = lcm(l, coins[i])
                    count += 1
            
            if count % 2:
                odd_lcm.append(l)
            else:
                even_lcm.append(l)

        def isGood(mid):
            total = 0
            
            for l in odd_lcm:
                total += mid // l
            
            for l in even_lcm:
                total -= mid // l
            
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
