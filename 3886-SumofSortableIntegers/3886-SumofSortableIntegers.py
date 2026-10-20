# Last updated: 10/20/2026, 5:28:57 PM
1class Solution:
2    def sortableIntegers(self, nums: list[int]) -> int:
3        n = len(nums)
4        sorted_nums = sorted(nums)
5        ans = 0
6
7        def getLCP(left, right):
8            k = right - left + 1
9            lcp = [0] * k
10            l = 0
11            for i in range(1, k):
12                while l > 0 and sorted_nums[i + left] != lcp[i]:
13                    l = lcp[l - 1]
14
15                if sorted_nums[i + left] == sorted_nums[l + left]:
16                    l += 1
17                    lcp[i] = l
18            return lcp
19
20        for i in range(n):
21            k = i + 1
22            if n % k != 0: continue
23
24            for sub in range(n//k):
25                left = sub * k
26                lcp = getLCP(left, left + k - 1)
27
28                index = 0
29                for l in range(left, left + k * 2):
30                    num = nums[left + (l % k)]
31
32                    while index > 0 and num != sorted_nums[left + index]:
33                        index = lcp[index - 1]
34
35                    if num == sorted_nums[left + index]:
36                        index += 1
37                        if index == k: break
38                else:
39                    break
40            else:
41                ans += k
42
43
44        return ans