# Last updated: 28/6/2025, 7:56:03 am
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ret = sorted(heap, key=lambda x: x[1])
        return [x for x, _ in ret]