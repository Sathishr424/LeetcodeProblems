# Last updated: 2/10/2025, 12:36:52 pm
class Solution:
    def maxBottlesDrunk(self, fullBottles: int, numExchange: int) -> int:
        drunk = 0
        empty = 0
        while fullBottles:
            drunk += fullBottles
            empty += fullBottles
            fullBottles = 0
            if empty >= numExchange:
                fullBottles += 1
                empty -= numExchange
                numExchange += 1
            # print(fullBottles, empty, numExchange, drunk)
        return drunk