# Last updated: 12/9/2025, 5:53:51 AM
1class Solution:
2    def findSmallestInteger(self, nums: List[int], value: int) -> int:
3        n = len(nums)
4
5        freq = defaultdict(int)
6        for num in nums:
7            freq[num % value] += 1
8        
9        for i in range(0, n+1):
10            if freq[i % value]:
11                freq[i % value] -= 1
12            else:
13                return i
14
15        return n + 2