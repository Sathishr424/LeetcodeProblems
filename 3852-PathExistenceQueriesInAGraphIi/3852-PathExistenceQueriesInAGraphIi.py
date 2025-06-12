# Last updated: 12/6/2025, 5:33:30 am
m = 19
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = []
        ret = []

        relation = [0] * n
        for i, num in enumerate(nums):
            arr.append((num, i))
        
        arr.sort()

        for i, (num, index) in enumerate(arr):
            relation[index] = i

        furthest = [0] * n
        for i in range(n):
            furthest[i] = bisect_right(arr, (arr[i][0]+maxDiff, float('inf'))) - 1
            if furthest[i] == i: furthest[i] = -1

        logs = [[-1] * n for _ in range(m)]

        for i in range(n):
            logs[0][i] = furthest[i]

        for i in range(1, m):
            for j in range(n):
                if logs[i-1][j] == -1: continue
                logs[i][j] = logs[i-1][logs[i-1][j]]

        @cache
        def getDistance(x, y):
            cnt = 0
            p = 0
            while True:
                if logs[p][x] >= y or logs[p][x] == -1:
                    if p == 0: break
                    else: p -= 1
                else:
                    x = logs[p][x]
                    cnt += 1 << p
                    p += 1
            
            return cnt+1 if logs[p][x] >= y else -1

        for x, y in queries:
            if x == y: 
                ret.append(0)
                continue

            x = relation[x]
            y = relation[y]

            if x > y:
                x, y = y, x
               
            ret.append(getDistance(x, y))

        return ret