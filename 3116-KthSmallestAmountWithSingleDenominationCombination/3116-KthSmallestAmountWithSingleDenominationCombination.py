# Last updated: 9/8/2025, 7:41:14 pm
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)

        def isGood(mid):
            total = 0
            
            def rec(index, cnt, l):
                nonlocal total
                if index == n:
                    if cnt == 0: return
                    if cnt % 2:
                        total += mid // l
                    else:
                        total -= mid // l
                    return
                
                rec(index + 1, cnt + 1, lcm(l, coins[index]))
                rec(index + 1, cnt, l)

            rec(0, 0, 1)
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
