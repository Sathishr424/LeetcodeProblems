# Last updated: 9/8/2025, 7:59:25 pm
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)

        odd_lcm = []
        even_lcm = []

        def rec(index, cnt, l):
            if index == n:
                if cnt == 0: return
                if cnt % 2:
                    odd_lcm.append(l)
                else:
                    even_lcm.append(l)
                return
            
            rec(index + 1, cnt + 1, lcm(l, coins[index]))
            rec(index + 1, cnt, l)

        rec(0, 0, 1)

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
