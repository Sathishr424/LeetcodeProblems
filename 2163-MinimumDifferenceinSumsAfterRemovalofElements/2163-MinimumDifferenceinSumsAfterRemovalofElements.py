# Last updated: 18/7/2025, 2:57:41 pm
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        quater = n // 3

        heap = []
        s = 0
        max_sum = [0] * (n + 1)
        for i in range(n-1, n-(quater*2)-1, -1):
            heapq.heappush(heap, nums[i])
            s += nums[i]
            if len(heap) > quater:
                s -= heapq.heappop(heap)
            if len(heap) == quater:
                max_sum[i] = max(max_sum[i + 1], s)

        left_end = n - quater

        heap = []
        s = 0
        ret = inf
        for i in range(n-quater):
            heapq.heappush(heap, -nums[i])
            s += nums[i]
            
            if len(heap) > quater:
                s -= -heapq.heappop(heap)
            if len(heap) == quater:
                ret = min(ret, s - max_sum[i + 1])

        return ret
                