# Last updated: 18/7/2025, 3:03:15 pm
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        quater = n // 3

        heap = []
        s = 0
        max_sum = [0] * (n + 1)

        for i in range(n-quater+1, n):
            heapq.heappush(heap, nums[i])
            s += nums[i]

        for i in range(n-quater, n-(quater*2)-1, -1):
            heapq.heappush(heap, nums[i])
            s += nums[i]
            max_sum[i] = cmax(max_sum[i + 1], s)
            
            s -= heapq.heappop(heap)

        heap = []
        s = 0
        ret = inf

        for i in range(quater-1):
            heapq.heappush(heap, -nums[i])
            s += nums[i]

        for i in range(quater-1, n-quater):
            heapq.heappush(heap, -nums[i])
            s += nums[i]
            ret = cmin(ret, s - max_sum[i + 1])

            s += heapq.heappop(heap)

        return ret
                