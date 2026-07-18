# Last updated: 7/18/2026, 7:24:53 PM
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
16            pairs = cnt * (cnt - 1) // 2
17
18            add = 2
19            while num * add <= m:
20                curr = ans[num * add]
21                pairs -= curr
22                add += 1
23            ans[num] = pairs
24
25        arr = []
26        prefix = []
27        cnt = 0
28        for num in sorted(list(ans.keys())):
29            cnt += ans[num]
30            if ans[num] > 0:
31                arr.append(num)
32                prefix.append(cnt)
33
34        m = len(arr)
35        ret = []
36        for q in queries:
37            q += 1
38            l = 0
39            r = m
40
41            while l < r:
42                mid = (l + r) // 2
43
44                if prefix[mid] >= q:
45                    r = mid
46                else:
47                    l = mid + 1
48            ret.append(arr[l])
49
50        return ret