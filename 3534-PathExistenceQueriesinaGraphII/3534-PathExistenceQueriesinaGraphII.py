# Last updated: 29/4/2025, 1:15:22 pm
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

        # print(furthest)
        # print(logs)

        for x, y in queries:
            if x == y: 
                ret.append(0)
                continue

            x = relation[x]
            y = relation[y]

            if x > y:
                x, y = y, x
            
            cnt = 0
            p = 0
            node = x
            
            while True:
                if logs[p][node] >= y or logs[p][node] == -1:
                    if p == 0:
                        if logs[p][node] != -1: 
                            cnt += 1
                            node = y
                        break
                    p = 0
                else:
                    node = logs[p][node]
                    cnt += 2 ** p
                    p += 1
            
            ret.append(cnt if node >= y else -1)

        return ret