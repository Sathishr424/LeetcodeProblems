# Last updated: 19/5/2025, 5:18:01 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
N = 10**5 + 1
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        first = segments[0][0]
        last = segments[0][0]

        start = [0] * N
        end = [0] * N

        for x, y, color in segments:
            first = cmin(first, x)
            last = cmax(last, y)
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