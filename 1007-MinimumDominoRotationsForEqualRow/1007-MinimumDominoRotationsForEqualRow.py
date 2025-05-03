# Last updated: 3/5/2025, 11:32:58 am
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        top_freq = [0] * 7
        max_top_freq = 1
        for num in tops:
            top_freq[num] += 1
            if top_freq[num] > top_freq[max_top_freq]:
                max_top_freq = num
        
        bottom_freq = [0] * 7
        max_bottom_freq = 1
        for num in bottoms:
            bottom_freq[num] += 1
            if bottom_freq[num] > bottom_freq[max_bottom_freq]:
                max_bottom_freq = num

        def checkRotation(x, y, z):
            rotation = 0
            for i in range(n):
                if x[i] != z:
                    if y[i] != z: return float('inf')
                    rotation += 1

            return rotation

        ret = min(checkRotation(tops, bottoms, max_top_freq), checkRotation(bottoms, tops, max_bottom_freq))

        return ret if ret != float('inf') else -1
        
        


