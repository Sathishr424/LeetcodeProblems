# Last updated: 22/4/2025, 2:14:26 am
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        A = SortedList()
        ans = 0
        for i, n in enumerate(nums):
            j = A.bisect_right(2*n)
            ans += (i - j)
            A.add(n)
        
        return ans