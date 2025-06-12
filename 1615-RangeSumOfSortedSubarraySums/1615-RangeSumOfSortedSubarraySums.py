# Last updated: 12/6/2025, 5:41:16 am
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        for _ in range(left-1):
            num, i = heapq.heappop(heap)
            if i+1 < n:
                heapq.heappush(heap, (num+nums[i+1], i+1))
        
        ret = 0
        for _ in range(right-left+1):
            num, i = heapq.heappop(heap)
            ret += num
            if i+1 < n:
                heapq.heappush(heap, (num+nums[i+1], i+1))

        return ret % mod
