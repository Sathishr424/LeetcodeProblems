# Last updated: 12/6/2025, 5:35:47 am
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        res = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            new_val = x * 2 + y
            heapq.heappush(nums, new_val)
            res += 1
        
        return res