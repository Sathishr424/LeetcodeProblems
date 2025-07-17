# Last updated: 17/7/2025, 3:02:37 pm
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)

        def getDis(a, b):
            diff = ((b[0] - a[0])**2) + ((b[1] - a[1])**2)
            return sqrt(diff)

        ret = 0
        dis = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if j == i: continue
                d = getDis(points[i], points[j])
                ret += dis[i][d] * 2
                dis[i][d] += 1
        
        return ret