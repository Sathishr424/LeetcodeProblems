# Last updated: 29/4/2025, 1:50:27 pm
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
            for i in range(m-1, -1, -1):
                if logs[i][x] < y and logs[i][x] != -1:
                    x = logs[i][x]
                    cnt += 1 << i
            
            return cnt+1 if logs[0][x] >= y else -1

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