# Last updated: 12/6/2025, 5:46:49 am
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for i in range( min(k, len(nums)) ):
            self.nums.append(nums[i])
        
        heapq.heapify(self.nums)

        for i in range(k, len(nums)):
            heapq.heappushpop(self.nums, nums[i])

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k: heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)