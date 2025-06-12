# Last updated: 12/6/2025, 5:43:43 am
class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        ret = [0] * n
        i = 0
        while candies > 0:
            ret[i % n] += min(candies, i+1)
            candies -= i + 1
            i += 1
        return ret 