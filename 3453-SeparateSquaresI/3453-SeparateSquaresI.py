# Last updated: 1/14/2026, 12:33:32 AM
1class Solution:
2    def separateSquares(self, squares: List[List[int]]) -> float:
3        n = len(squares)
4        left = 0
5        right = 0
6
7        for x, y, l in squares:
8            left = min(y, left)
9            right = max(y+l, right)
10        
11        precision = 1 / (10**5)
12        while right - left > precision:
13            mid = (left+right) / 2
14
15            top = 0
16            bottom = 0
17
18            for x, y, l in squares:
19                if y < mid and y+l > mid:
20                    b = mid-y
21                    t = l - b
22                    top += t * l
23                    bottom += b * l
24                elif y < mid:
25                    bottom += l*l
26                else:
27                    top += l*l
28            
29            if top > bottom:
30                left = mid
31            else:
32                right = mid
33
34        return left