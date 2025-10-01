# Last updated: 1/10/2025, 10:57:26 am
class Solution:
    def numWaterBottles(self, n: int, exchange: int) -> int:
        cnt = n
        while n >= exchange:
            d = n // exchange
            cnt += d
            rem = n % exchange
            n = rem + d
        
        return cnt