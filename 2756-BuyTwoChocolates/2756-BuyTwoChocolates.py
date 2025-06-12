# Last updated: 12/6/2025, 5:37:01 am
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = float('inf')
        second = float('inf')
        for price in prices:
            if price < first:
                second = first
                first = price
            elif price < second:
                second = price
        
        if first+second <= money: return money - (first+second)
        return money