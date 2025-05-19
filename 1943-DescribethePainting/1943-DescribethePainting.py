# Last updated: 19/5/2025, 5:08:45 pm
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        starts = defaultdict(int)
        ends = defaultdict(int)

        first = segments[0][0]
        last = segments[0][0]

        for x, y, color in segments:
            starts[x] += color
            ends[y] += color
            first = min(first, x)
            last = max(last, y)
        
        ret = []
        prev = first
        mix = 0
        for index in range(first, last+1):
            if index in ends:
                ret.append([prev, index, mix])
                mix -= ends[index]
                prev = index
            if index in starts:
                if prev != index and mix > 0:
                    ret.append([prev, index, mix])
                mix += starts[index]
                prev = index

        return ret