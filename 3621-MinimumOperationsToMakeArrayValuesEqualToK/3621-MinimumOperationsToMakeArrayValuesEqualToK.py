# Last updated: 12/6/2025, 5:35:24 am
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        mini = nums[0]
        for num in nums:
            counts[num] = 1
            mini = min(num, mini)
        
        if mini >= k:
            return len(counts) - (mini == k)
        
        return -1