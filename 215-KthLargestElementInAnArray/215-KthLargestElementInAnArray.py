# Last updated: 12/6/2025, 5:51:36 am
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(k):
            arr.append(nums[i])
        
        heapq.heapify(arr)

        for i in range(k, len(nums)):
            heapq.heappushpop(arr, nums[i])
        
        return arr[0]