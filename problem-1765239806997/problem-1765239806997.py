# Last updated: 12/9/2025, 5:53:26 AM
1class Solution:
2    def findSmallestInteger(self, nums: List[int], value: int) -> int:
3        n = len(nums)
4
5        rems = []
6        for num in nums:
7            rems.append(num % value)
8
9        rems.sort()
10        freq = defaultdict(int)
11        for num in rems:
12            freq[num] += 1
13        
14        for i in range(0, n+1):
15            if freq[i % value]:
16                freq[i % value] -= 1
17            else:
18                return i
19
20        return n + 2