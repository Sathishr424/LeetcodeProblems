# Last updated: 19/5/2025, 5:06:10 pm
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        starts = defaultdict(int)
        ends = defaultdict(int)

        r = 0
        for x, y, color in segments:
            starts[x] += color
            ends[y] += color
            r = max(r, y)
        
        segments.sort(key=lambda x: (x[0], x[1]))
        ret = []
        prev = segments[0][0]
        def rec(start, mix):
            nonlocal ret, prev, r
            if start > r: return
            if start in ends:
                ret.append([prev, start, mix])
                mix -= ends[start]
                prev = start
            if start in starts:
                if prev != start and mix > 0:
                    ret.append([prev, start, mix])
                mix += starts[start]
                prev = start
            rec(start+1, mix)
        
        rec(segments[0][0], 0)
        return ret