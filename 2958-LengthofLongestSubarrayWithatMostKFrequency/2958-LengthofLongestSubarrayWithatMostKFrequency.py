# Last updated: 8/12/2026, 9:43:58 AM
1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4
5        freq = defaultdict(int)
6        left = 0
7        best = 1
8        for i in range(n):
9            freq[nums[i]] += 1
10
11            while freq[nums[i]] > k:
12                freq[nums[left]] -= 1
13                left += 1
14
15            best = max(best, i - left + 1)
16
17        return best