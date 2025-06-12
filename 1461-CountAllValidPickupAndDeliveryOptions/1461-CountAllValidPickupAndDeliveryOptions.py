# Last updated: 12/6/2025, 5:42:12 am
import math
class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 1
        for i in range(2, n+1):
            tmp = (i*2) - 1
            ans *= (tmp * (tmp+1)) // 2
            ans %= mod 
        return ans

        