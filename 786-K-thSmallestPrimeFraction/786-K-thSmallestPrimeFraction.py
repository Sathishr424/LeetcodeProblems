# Last updated: 9/8/2025, 4:33:52 am
class Solution:
    def kthSmallestPrimeFraction(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        heap = []
        for i in range(n-1):
            heapq.heappush(heap, (nums[i] / nums[n-1], i, n-1))

        while k-1:
            _, i, j = heapq.heappop(heap)

            if j-1 > i:
                j -= 1
                heapq.heappush(heap, (nums[i] / nums[j], i, j))
            k -= 1
        
        _, i, j = heapq.heappop(heap)
        return [nums[i], nums[j]]