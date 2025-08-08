# Last updated: 9/8/2025, 4:45:05 am
class Solution:
    def kthSmallestPrimeFraction(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k = (n * (n-1) // 2) - k + 1
    
        heap = []
        for i in range(n-1):
            heapq.heappush(heap, (-nums[i] / nums[i+1], i, i+1))

        for _ in range(k-1):
            _, i, j = heapq.heappop(heap)

            if j+1 < n:
                j += 1
                heapq.heappush(heap, (-nums[i] / nums[j], i, j))
        
        _, i, j = heapq.heappop(heap)
        return [nums[i], nums[j]]