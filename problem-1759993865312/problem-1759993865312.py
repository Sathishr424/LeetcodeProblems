# Last updated: 9/10/2025, 12:41:05 pm
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        heap = []
        for num in nums:
            heap.append(-num)
        heapq.heapify(heap)
        
        score = 0
        while k:
            num = -heapq.heappop(heap)

            score += num
            heapq.heappush(heap, -ceil(num / 3))
            k -= 1

        return score