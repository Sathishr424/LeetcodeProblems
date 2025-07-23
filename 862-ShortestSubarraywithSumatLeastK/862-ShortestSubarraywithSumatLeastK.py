# Last updated: 23/7/2025, 5:51:58 pm
cmin = lambda x, y: x if x < y else y
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        s = 0
        ret = inf
        # prefix = [0]
        # for num in nums:
        #     prefix.append(prefix[-1] + num)
    
        heap = []
        heapq.heappush(heap, (0, -1))
        for i in range(n):
            s += nums[i]
            heapq.heappush(heap, (s, i))
            
            while heap and s - heap[0][0] >= k:
                c, p = heapq.heappop(heap)
                ret = cmin(ret, i - p)
        
        if ret == inf: return -1
        return ret