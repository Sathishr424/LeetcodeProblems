# Last updated: 14/6/2025, 2:38:34 pm
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets = defaultdict(int)
        ret = 0

        for i in range(len(nums)-1):
            if nums[i] == key:
                targets[nums[i+1]] += 1
                ret = nums[i+1]

        for num in targets:
            if targets[num] > targets[ret]:
                ret = num
        
        return ret