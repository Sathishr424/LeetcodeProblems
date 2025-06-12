# Last updated: 12/6/2025, 5:44:27 am
inf = 10**4 * 2
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        def checkRotation(x, y, z):
            rotation = 0
            for i in range(n):
                if x[i] != z:
                    if y[i] != z: return inf
                    rotation += 1

            return rotation

        ret = min(checkRotation(tops, bottoms, tops[0]), checkRotation(bottoms, tops, bottoms[0]), checkRotation(tops, bottoms, bottoms[0]), checkRotation(bottoms, tops, tops[0]))

        return ret if ret != inf else -1
        
        


