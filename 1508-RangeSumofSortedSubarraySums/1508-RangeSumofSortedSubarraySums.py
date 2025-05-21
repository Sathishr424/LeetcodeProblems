# Last updated: 22/5/2025, 12:57:42 am
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        index = 1
        ret = 0
        while index < left:
            num, i = heapq.heappop(heap)
            if i+1 < n:
                heapq.heappush(heap, (num+nums[i+1], i+1))
            index += 1
        
        while index <= right:
            num, i = heapq.heappop(heap)
            ret += num
            if i+1 < n:
                heapq.heappush(heap, (num+nums[i+1], i+1))
            index += 1

        return ret % mod
