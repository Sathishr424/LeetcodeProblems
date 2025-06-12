# Last updated: 12/6/2025, 5:41:29 am
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        ret = []
        for i in range(n):
            val = prices[i]
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    val -= prices[j]
                    break
            ret.append(val)
        
        return ret