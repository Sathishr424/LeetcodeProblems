# Last updated: 8/18/2026, 2:06:51 PM
1class Solution:
2    def largestInteger(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4
5        if k == n: return max(nums)
6        freq =  Counter(nums)
7
8        if k == 1:
9            for num in sorted(list(set(freq)), reverse=True):
10                if freq[num] == 1: return num
11            return -1
12
13        left = nums[0]
14        right = nums[-1]
15
16        if freq[left] == 1 and freq[right] == 1:
17            return max(left, right)
18        elif freq[left] == 1:
19            return left
20        elif freq[right] == 1:
21            return right
22
23        return -1