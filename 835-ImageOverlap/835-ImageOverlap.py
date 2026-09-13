# Last updated: 9/13/2026, 7:27:03 PM
1class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4
5        def overlapScore(i2, j2):
6            score = 0
7            for i in range(n):
8                for j in range(n):
9                    if img1[i][j] != 1: continue
10                    ni = i + i2
11                    nj = j + j2
12
13                    if 0 <= ni < n and 0 <= nj < n and img2[ni][nj] == 1:
14                        score += 1
15            return score
16
17        best = 0
18        for i in range(-n+1, n):
19            for j in range(-n+1, n):
20                best = max(best, overlapScore(i, j))
21
22        return best