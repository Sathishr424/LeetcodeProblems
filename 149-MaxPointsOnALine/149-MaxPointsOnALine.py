# Last updated: 12/6/2025, 5:52:20 am
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ret = 1
        for i in range(len(points)):
            hash = defaultdict(int)
            for j in range(i+1, len(points)):
                y = points[j][1] - points[i][1]
                x = points[j][0] - points[i][0]

                if x == 0:
                    diff = float('inf')
                else:
                    diff = y/x

                hash[diff] += 1
                ret = max(ret, hash[diff]+1)
        
        return ret