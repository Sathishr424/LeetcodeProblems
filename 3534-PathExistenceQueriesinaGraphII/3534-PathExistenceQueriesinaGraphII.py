# Last updated: 29/4/2025, 1:38:24 pm
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

        logs = [[-1] * n for _ in range(m)]

        for i in range(n):
            logs[0][i] = furthest[i]

        for i in range(1, m):
            for j in range(n):
                logs[i][j] = logs[i-1][logs[i-1][j]]

        for x, y in queries:
            if x == y: 
                ret.append(0)
                continue

            x = relation[x]
            y = relation[y]

            if x > y:
                x, y = y, x
            
            if logs[m-1][x] < y:
                ret.append(-1)
                continue
            
            cnt = 0
            node = x
            
            for i in range(m-1, -1, -1):
                if logs[i][node] < y:
                    node = logs[i][node]
                    cnt += 1 << i
                    
            ret.append(cnt+1)

        return ret