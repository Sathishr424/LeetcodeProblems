# Last updated: 16/4/2025, 11:03:35 pm
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        p_index = bisect_left(nums, 1)
        if p_index == 0: return []

        index = 0
        zeros = 0
        pos = {}
        for num in nums:
            zeros += (num == 0)
        
        ret = []
        if zeros >= 3: ret.append([0, 0, 0])
        added = {}

        for i in range(p_index, n):
            pos[nums[i]] = 1
        
        neg = {}
        for i in range(0, p_index):
            neg[nums[i]] = 1
            for j in range(i+1, p_index):
                s = -(nums[i]+nums[j])
                if s in pos:
                    mask = hash((nums[i], nums[j], s))
                    if mask not in added:
                        ret.append([nums[i], nums[j], s])
                        added[mask] = 1
        
        for i in range(p_index, n):
            for j in range(i+1, n):
                s = -(nums[i]+nums[j])
                if s in neg:
                    mask = hash((s, nums[i], nums[j]))
                    if mask not in added:
                        ret.append([nums[i], nums[j], s])
                        added[mask] = 1

        return ret


