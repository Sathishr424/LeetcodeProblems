# Last updated: 16/10/2025, 4:04:02 pm
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        if value == 1: return n
        N = 10**9
        for i in range(n):
            l = -N
            r = N
            num = nums[i]

            while l < r:
                mid = (l + r) // 2

                if num + (value * mid) >= value:
                    r = mid
                else:
                    l = mid + 1
            nums[i] += (value * (l - 1))
        nums.sort()

        # print(nums)
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        prev = heapq.heappop(heap)
        if prev != 0: return 0
        while heap:
            num = heapq.heappop(heap)
            if num == prev:
                heapq.heappush(heap, num + value)
            elif num != prev + 1: return prev + 1
            prev = num
        
        return n