# Last updated: 12/9/2025, 5:53:36 AM
1class Solution:
2    def findSmallestInteger(self, nums: List[int], value: int) -> int:
3        n = len(nums)
4
5        rems = []
6        for num in nums:
7            rems.append(num % value)
8
9        freq = defaultdict(int)
10        for num in rems:
11            freq[num] += 1
12        
13        for i in range(0, n+1):
14            if freq[i % value]:
15                freq[i % value] -= 1
16            else:
17                return i
18
19        return n + 2