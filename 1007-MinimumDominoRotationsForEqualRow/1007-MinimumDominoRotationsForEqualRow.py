# Last updated: 3/5/2025, 11:36:17 am
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        def checkRotation(x, y, z):
            rotation = 0
            for i in range(n):
                if x[i] != z:
                    if y[i] != z: return float('inf')
                    rotation += 1

            return rotation

        ret = min(checkRotation(tops, bottoms, tops[0]), checkRotation(bottoms, tops, bottoms[0]), checkRotation(tops, bottoms, bottoms[0]), checkRotation(bottoms, tops, tops[0]))

        return ret if ret != float('inf') else -1
        
        


