# Last updated: 9/4/2025, 12:44:08 pm
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        n = len(nums)

        op = 0
        for i in range(n-2, -1, -1):
            if counts[nums[i+1]] == n-i-1:
                op += 1
                counts[nums[i]] += counts[nums[i+1]]

        if counts[nums[0]] == n and nums[0] >= k:
            return op + (nums[0] != k)
        
        return -1