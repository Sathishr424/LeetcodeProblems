# Last updated: 2/10/2025, 8:34:34 pm
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        coins.sort()

        def isGood(mid):
            total = 0
            def rec(index, rem, l, is_odd):
                nonlocal total
                if index == n:
                    if rem == 0:
                        if is_odd:
                            total -= mid // l
                        else:
                            total += mid // l
                    return
                
                rec(index + 1, rem, l, is_odd)
                if rem: rec(index + 1, rem - 1, lcm(l, coins[index]), is_odd)

            for group in range(1, n+1):
                rec(0, group, 1, group % 2 == 0)
            
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
