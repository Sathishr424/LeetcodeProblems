# Last updated: 12/27/2025, 8:35:05 PM
1class Solution:
2    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
3        n = len(nums)
4
5        need = defaultdict(int)
6        top = defaultdict(int)
7        both = defaultdict(lambda: defaultdict(int))
8        bottom = defaultdict(int)
9
10        s = 0
11        maxi = 0
12        for i in range(n):
13            num = nums[i]
14            fb = forbidden[i]
15
16            if num == fb:
17                s += 1
18                need[num] += 1
19                maxi = max(maxi, need[num])
20            
21            top[num] += 1
22            bottom[fb] += 1
23            both[num][fb] += 1
24    
25        for num in need:
26            cnt = top[num] + bottom[num] - both[num][num]
27            rem = n - cnt
28            if rem < need[num]: return -1
29
30        return max(maxi, (s + 1) // 2)