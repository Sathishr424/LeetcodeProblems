# Last updated: 25/6/2025, 7:53:08 am
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_heap = []
        max_heap = []
        
        prev = 0
        ret = 1
        for i in range(n):
            heapq.heappush(min_heap, (nums[i], i))
            heapq.heappush(max_heap, (-nums[i], i))

            while min_heap and min_heap[0][1] < prev:
                heapq.heappop(min_heap)
                
            while max_heap and max_heap[0][1] < prev:
                heapq.heappop(max_heap)
            
            while (-max_heap[0][0]) - min_heap[0][0] > limit:
                prev += 1
                while min_heap and min_heap[0][1] < prev:
                    heapq.heappop(min_heap)
                    
                while max_heap and max_heap[0][1] < prev:
                    heapq.heappop(max_heap)
            
            ret = max(ret, i - prev + 1)
        
        return ret