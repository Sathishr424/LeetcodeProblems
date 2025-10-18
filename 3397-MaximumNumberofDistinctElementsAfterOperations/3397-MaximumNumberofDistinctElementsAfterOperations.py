# Last updated: 18/10/2025, 2:17:47 pm
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()
        arr = []
        arr.append(nums[0] - k)

        for i in range(1, n):
            if nums[i] - k <= arr[-1]:
                num = min(nums[i] + k, arr[-1] + 1)
            else:
                num = nums[i] - k
            arr.append(num)
        
        return len(set(arr))