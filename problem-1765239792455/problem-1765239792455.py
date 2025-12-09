# Last updated: 12/9/2025, 5:53:12 AM
1class Solution:
2    def findSmallestInteger(self, nums: List[int], value: int) -> int:
3        n = len(nums)
4        # if (value == 1): return n
5
6        rems = []
7        for num in nums:
8            rems.append(num % value)
9
10        rems.sort()
11        freq = defaultdict(int)
12        for num in rems:
13            freq[num] += 1
14        
15        for i in range(0, n+1):
16            if freq[i]:
17                freq[i] -= 1
18                continue
19            if freq[i % value]:
20                freq[i % value] -= 1
21            else:
22                return i
23
24        return n + 2