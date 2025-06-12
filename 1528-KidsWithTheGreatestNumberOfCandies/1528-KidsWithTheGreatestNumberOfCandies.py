# Last updated: 12/6/2025, 5:41:48 am
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        gc = max(candies)
        ret = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= gc:
                ret.append(True)
            else: ret.append(False)
        return ret