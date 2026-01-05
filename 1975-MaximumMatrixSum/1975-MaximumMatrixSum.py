# Last updated: 1/5/2026, 12:38:23 PM
1inf = float('inf')
2class Solution:
3    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
4        n = len(matrix)        
5
6        neg = 0
7        minNum = inf
8        ans = 0
9        for i in range(n):
10            for j in range(n):
11                neg += matrix[i][j] < 0
12                minNum = min(minNum, abs(matrix[i][j]))
13                ans += abs(matrix[i][j])
14        
15        if neg % 2 == 0:
16            return ans
17        
18        return ans - minNum * 2
19
20