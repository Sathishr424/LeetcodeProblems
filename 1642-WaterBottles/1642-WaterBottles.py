# Last updated: 12/6/2025, 5:41:07 am
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles
        empty = numBottles

        while empty >= numExchange:
            exchange = empty // numExchange
            rem = empty % numExchange
            ret += exchange
            empty = rem + exchange
        
        return ret