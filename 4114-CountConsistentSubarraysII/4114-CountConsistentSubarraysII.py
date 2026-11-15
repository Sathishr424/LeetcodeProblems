# Last updated: 11/15/2026, 10:40:00 PM
1class Solution:
2    def countConsistent(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        # sparse table for range AND
6        sp = [nums[:]]
7        j = 1
8        while (1 << j) <= n:
9            prev, h = sp[-1], 1 << (j - 1)
10            sp.append([prev[i] & prev[i + h] for i in range(n - (1 << j) + 1)])
11            j += 1
12
13        def q(l, r):
14            k = (r - l + 1).bit_length() - 1
15            row = sp[k]
16            return row[l] & row[r - (1 << k) + 1]
17
18        def getLeft(index):
19            l, r = 0, index
20            target = nums[index]
21            while l < r:
22                mid = (l + r) // 2
23                if q(mid, index) == target:
24                    r = mid
25                else:
26                    l = mid + 1
27            return l
28
29        def getRight(index):
30            l, r = index, n - 1
31            target = nums[index]
32            while l < r:
33                mid = (l + r + 1) // 2
34                if q(index, mid) == target:
35                    l = mid
36                else:
37                    r = mid - 1
38            return l
39
40        ans = 0
41        prevs = {}
42        for i in range(n):
43            left = getLeft(i)
44            right = getRight(i)
45            l = i - max(left, prevs.get(nums[i], -1) + 1) + 1
46            r = right - i + 1
47            if right > i:
48                prevs[nums[i]] = i
49            ans += l * r
50        return ans