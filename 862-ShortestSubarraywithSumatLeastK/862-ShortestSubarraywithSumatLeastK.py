# Last updated: 23/7/2025, 5:50:50 pm
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        s = 0
        prev = 0
        ret = inf

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def getNewHeap(heap, prev, b_prev):
            new_heap = []
            for c, j in heap:
                if j < prev: continue

                c -= prefix[prev] - prefix[b_prev]
                heapq.heappush(new_heap, (c, j))
            return new_heap
        
        heap = []
        heapq.heappush(heap, (0, -1))
        for i in range(n):
            s += nums[i]
            heapq.heappush(heap, (s, i))
            
            # if b_prev == prev: continue
            diff = 0
            while heap and s - heap[0][0] >= k:
                c, p = heapq.heappop(heap)
                # print(nums[p+1:i+1])
                ret = min(ret, i - p)
                prev = p + 1

            # print(heap, 'update')
            # print(nums[prev:i+1], (prev, i), s)
        
        if ret == inf: return -1
        return ret