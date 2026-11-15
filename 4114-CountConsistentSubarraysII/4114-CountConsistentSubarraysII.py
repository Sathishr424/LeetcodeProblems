# Last updated: 11/15/2026, 11:29:12 PM
1class Solution:
2    def countConsistent(self, nums: list[int]) -> int:
3        n = len(nums)
4        m = 20
5        ans = 0
6
7        LEFT = [[1] * n for _ in range(m)]
8        RIGHT = [[1] * n for _ in range(m)]
9        for b in range(m):
10            i = 0
11            while i < n:
12                start = i
13                while i < n and nums[i] & (1 << b):
14                    i += 1
15
16                j = i - 1
17                while j >= start:
18                    RIGHT[b][j] = i - j
19                    LEFT[b][j] = j - start + 1
20                    j -= 1
21
22                i = max(i + 1, i)
23
24        left_index = [0] * n
25        right_index = [0] * n
26        for i in range(n):
27            min_r = n-1
28            min_l = 0
29            for b in range(m):
30                if nums[i] & (1 << b):
31                    min_r = min(min_r, i + RIGHT[b][i] - 1)
32                    min_l = max(min_l, i - LEFT[b][i] + 1)
33            
34            left_index[i] = min_l
35            right_index[i] = min_r
36
37        def getLeft(index):
38            return left_index[index]
39
40        def getRight(index):
41            return right_index[index]
42
43        prevs = defaultdict(lambda: -1)
44        for i in range(n):
45            left = getLeft(i)
46            right = getRight(i)
47
48            l = i - max(left, prevs[nums[i]] + 1) + 1
49            r = right - i + 1
50            if right > i:
51                prevs[nums[i]] = i
52            ans += l * r
53
54        return ans