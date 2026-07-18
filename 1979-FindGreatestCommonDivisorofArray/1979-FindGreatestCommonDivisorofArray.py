# Last updated: 7/18/2026, 7:20:00 PM
1class Solution:
2    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
3        n = len(nums)
4
5        m = max(nums)
6        divs = [0] * (m + 1)
7        for num in nums:
8            divs[num] += 1
9        for i in range(1, m + 1):
10            for j in range(i * 2, m + 1, i):
11                divs[i] += divs[j]
12
13        ans = defaultdict(int)
14        for num in range(m, 0, -1):
15            cnt = divs[num]
16            if cnt == 0: continue
17            pairs = cnt * (cnt - 1) // 2
18
19            add = 2
20            while num * add <= m:
21                if num * add in ans:
22                    curr = ans[num * add]
23                    pairs -= curr
24                add += 1
25            ans[num] = pairs
26
27        arr = []
28        freq = []
29        prefix = []
30        cnt = 0
31        for num in sorted(list(ans.keys())):
32            cnt += ans[num]
33            if ans[num] > 0:
34                arr.append(num)
35                freq.append(ans[num])
36                prefix.append(cnt)
37
38        m = len(arr)
39        ret = []
40        for q in queries:
41            q += 1
42            l = 0
43            r = m
44
45            while l < r:
46                mid = (l + r) // 2
47
48                if prefix[mid] >= q:
49                    r = mid
50                else:
51                    l = mid + 1
52            ret.append(arr[l])
53
54        return ret