# Last updated: 22/5/2025, 12:55:57 am
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        heap = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        index = 0
        ret = 0
        while heap:
            num, i = heapq.heappop(heap)
            index += 1
            if index >= left:
                ret += num
                if index == right: break
            if i+1 < n:
                heapq.heappush(heap, (num+nums[i+1], i+1))
        
        return ret % mod
