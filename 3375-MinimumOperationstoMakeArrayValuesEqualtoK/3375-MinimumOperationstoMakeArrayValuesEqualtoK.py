# Last updated: 9/4/2025, 12:54:11 pm
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        mini = nums[0]
        for num in nums:
            counts[num] += 1
            mini = min(num, mini)
        
        if mini >= k:
            return len(counts) - (mini == k)
        
        return -1