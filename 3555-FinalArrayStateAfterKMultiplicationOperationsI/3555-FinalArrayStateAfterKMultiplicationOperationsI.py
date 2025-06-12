# Last updated: 12/6/2025, 5:35:26 am
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1: return nums

        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        
        heapq.heapify(arr)

        for i in range(k):
            _, index = heapq.heappop(arr)
            nums[index] *= multiplier
            heapq.heappush(arr, (nums[index], index))
        
        return nums
