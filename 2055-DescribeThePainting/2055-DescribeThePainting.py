# Last updated: 12/6/2025, 5:39:21 am
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        first = segments[0][0]
        last = segments[0][0]

        for x, y, color in segments:
            first = cmin(first, x)
            last = cmax(last, y)
        
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
            elif start[index] and mix > 0 and prev != index:
                ret.append([prev, index, mix])
                prev = index
            
            if start[index]:
                mix += start[index]
                prev = index

        return ret