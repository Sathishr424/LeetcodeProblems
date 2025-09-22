# Last updated: 22/9/2025, 11:23:05 pm
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        max_sum = sum([max(0, num) for num in nums])
        vals = sorted([abs(num) for num in nums])

        heap = [(-max_sum, 0)]
        ans = 0
        while k:
            ans, index = heapq.heappop(heap)
            ans = -ans

            if index < n:
                heapq.heappush(heap, (-(ans - vals[index]), index + 1))
                if index > 0:
                    heapq.heappush(heap, (-(ans - vals[index] + vals[index - 1]), index + 1))
            k -= 1
        
        return ans