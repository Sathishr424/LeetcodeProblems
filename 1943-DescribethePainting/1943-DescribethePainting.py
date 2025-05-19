# Last updated: 19/5/2025, 5:10:34 pm
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        first = segments[0][0]
        last = segments[0][0]

        for x, y, color in segments:
            first = min(first, x)
            last = max(last, y)
        
        start = [0] * (last+1)
        end = [0] * (last+1)

        for x, y, color in segments:
            start[x] += color
            end[y] += color
        
        ret = []
        prev = first
        mix = 0
        for index in range(first, last+1):
            if end[index]:
                ret.append([prev, index, mix])
                mix -= end[index]
                prev = index
            if start[index]:
                if prev != index and mix > 0:
                    ret.append([prev, index, mix])
                mix += start[index]
                prev = index

        return ret