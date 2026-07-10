# Last updated: 7/11/2026, 3:42:22 AM
1m = 19
2class Solution:
3    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
4        arr = []
5        ret = []
6
7        relation = [0] * n
8        for i, num in enumerate(nums):
9            arr.append((num, i))
10        
11        arr.sort()
12
13        for i, (num, index) in enumerate(arr):
14            relation[index] = i
15
16        furthest = [0] * n
17        for i in range(n):
18            furthest[i] = bisect_right(arr, (arr[i][0]+maxDiff, float('inf'))) - 1
19            if furthest[i] == i: furthest[i] = -1
20
21        logs = [[-1] * n for _ in range(m)]
22
23        for i in range(n):
24            logs[0][i] = furthest[i]
25
26        for i in range(1, m):
27            for j in range(n):
28                if logs[i-1][j] == -1: continue
29                logs[i][j] = logs[i-1][logs[i-1][j]]
30
31        @cache
32        def getDistance(x, y):
33            cnt = 0
34            p = 0
35            while True:
36                if logs[p][x] >= y or logs[p][x] == -1:
37                    if p == 0: break
38                    else: p -= 1
39                else:
40                    x = logs[p][x]
41                    cnt += 1 << p
42                    p += 1
43            
44            return cnt+1 if logs[p][x] >= y else -1
45
46        for x, y in queries:
47            if x == y: 
48                ret.append(0)
49                continue
50
51            x = relation[x]
52            y = relation[y]
53
54            if x > y:
55                x, y = y, x
56               
57            ret.append(getDistance(x, y))
58
59        return ret