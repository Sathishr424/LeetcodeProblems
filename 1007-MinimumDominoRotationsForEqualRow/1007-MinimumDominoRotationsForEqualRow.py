# Last updated: 3/5/2025, 11:30:12 am
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
        
        # print(max_top_freq, max_bottom_freq)

        match = True
        rotation = 0
        for i in range(n):
            if tops[i] != max_top_freq:
                if bottoms[i] != max_top_freq:
                    match = False
                    break
                rotation += 1
        # print(match, rotation)
        ret = rotation if match else -1

        rotation = 0
        match = True
        for i in range(n):
            if bottoms[i] != max_bottom_freq:
                if tops[i] != max_bottom_freq:
                    match = False
                    break
                rotation += 1
        
        # print(match, rotation)
        if match:
            if ret == -1: ret = rotation
            else: ret = min(rotation, ret)

        return ret
        
        


