# Last updated: 25/6/2025, 7:28:23 am
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        ret = []
        ret.append(-heap[0][0])
        for i in range(k, n):
            heapq.heappush(heap, (-nums[i], i))
            left = i - k
            while heap and heap[0][1] <= left:
                heapq.heappop(heap)
            ret.append(-heap[0][0])

        return ret