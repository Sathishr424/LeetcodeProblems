# Last updated: 14/6/2025, 2:36:46 pm
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        keys = defaultdict(int)
        ret = 0

        for i in range(len(nums)-1):
            if nums[i] == key:
                keys[nums[i+1]] += 1
                ret = nums[i+1]

        for num in keys:
            if keys[num] > keys[ret]:
                ret = num
        
        return ret