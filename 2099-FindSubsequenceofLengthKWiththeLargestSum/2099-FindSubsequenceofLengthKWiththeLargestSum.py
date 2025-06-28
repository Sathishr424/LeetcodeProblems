# Last updated: 28/6/2025, 7:56:52 am
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x for x, _ in sorted(heap, key=lambda x: x[1])]