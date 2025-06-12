# Last updated: 12/6/2025, 5:40:59 am
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ret = 0
        n = len(piles)

        for i in range((n-1)-1, (n//3)-1, -2):
            ret += piles[i]
        return ret
