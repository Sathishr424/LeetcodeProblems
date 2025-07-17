# Last updated: 17/7/2025, 3:05:51 pm
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)

        @cache
        def getDis(x1, y1, x2, y2):
            diff = (x2 - x1)**2 + (y2 - y1)**2
            return sqrt(diff)

        ret = 0
        dis = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if j == i: continue
                d = getDis(points[i][0], points[i][1], points[j][0], points[j][1])
                ret += dis[i][d] * 2
                dis[i][d] += 1
        getDis.cache_clear()
        return ret