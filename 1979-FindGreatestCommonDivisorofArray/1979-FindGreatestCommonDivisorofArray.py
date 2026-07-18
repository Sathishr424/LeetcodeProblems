# Last updated: 7/18/2026, 7:20:50 PM
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
20                if num * add in ans:
21                    curr = ans[num * add]
22                    pairs -= curr
23                add += 1
24            ans[num] = pairs
25
26        arr = []
27        prefix = []
28        cnt = 0
29        for num in sorted(list(ans.keys())):
30            cnt += ans[num]
31            if ans[num] > 0:
32                arr.append(num)
33                prefix.append(cnt)
34
35        m = len(arr)
36        ret = []
37        for q in queries:
38            q += 1
39            l = 0
40            r = m
41
42            while l < r:
43                mid = (l + r) // 2
44
45                if prefix[mid] >= q:
46                    r = mid
47                else:
48                    l = mid + 1
49            ret.append(arr[l])
50
51        return ret