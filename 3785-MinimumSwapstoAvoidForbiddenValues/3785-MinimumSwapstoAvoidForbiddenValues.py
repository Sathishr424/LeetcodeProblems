# Last updated: 12/27/2025, 8:32:19 PM
1class Solution:
2    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
3        n = len(nums)
4
5        need = defaultdict(int)
6        top = defaultdict(int)
7        both = defaultdict(lambda: defaultdict(int))
8        bottom = defaultdict(int)
9
10        for i in range(n):
11            num = nums[i]
12            fb = forbidden[i]
13
14            if num == fb:
15                need[num] += 1
16            
17            top[num] += 1
18            bottom[fb] += 1
19            both[num][fb] += 1
20    
21        for num in need:
22            cnt = top[num] + bottom[num] - both[num][num]
23            rem = n - cnt
24            if rem < need[num]: return -1
25
26        op = 0
27        arr = [need[num] for num in need]
28        if len(arr) == 0: return op
29
30        s = sum(arr)
31        return max(max(arr), (s + 1) // 2)