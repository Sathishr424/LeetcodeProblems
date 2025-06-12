# Last updated: 12/6/2025, 5:39:55 am
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        used = {}
        while n > 0:
            prev = n
            val = min(n//3, 16)

            for i in range(val, -1, -1):
                if i in used: continue
                curr = 3**i
                if curr <= n:
                    used[i] = 1
                    n -= curr
                    break
            
            if n == prev: return False
            
        return n == 0