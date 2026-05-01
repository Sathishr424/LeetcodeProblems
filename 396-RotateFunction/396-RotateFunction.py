# Last updated: 5/1/2026, 6:18:29 PM
1class Solution:
2    def maxRotateFunction(self, nums: List[int]) -> int:
3        n = len(nums)
4        best = 0
5
6        right = 0
7        prefix = [0]
8        for i in range(n):
9            right += i * nums[i]
10            prefix.append(prefix[-1] + nums[i])
11
12        best = right
13        left = 0
14        for i in range(1, n):
15            left += nums[i-1] * (n-1)
16            left -= prefix[i-1]
17            r = prefix[-1] - prefix[i]
18            right -= r
19            # print(i, (left, right), left + right, nums[:i], nums[i:])
20            # l = 0
21            # r = 0
22            # for j in range(i, n):
23            #     l += nums[j % n] * (j - i)
24            # diff = n - i
25            # for j in range(i):
26            #     r += nums[j] * diff
27            #     diff += 1
28                
29            # print((r, l), l + r)
30            best = max(best, left + right)
31        
32        return best
33